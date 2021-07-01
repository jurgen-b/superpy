
# Imports
import argparse
import csv
import datetime
import os
import get_data as get
import output

# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'
# Your code below this line.


current_directory = os.getcwd()
data_dir = os.path.join(current_directory,'data')

#all functions

# Function to create a directory with the files needed for functions if not present.
# if present get products and date from files !!

def create_files():
    os.mkdir(data_dir)
    today_txt=os.path.join(data_dir,'today.txt')
    with open(os.path.join(data_dir,'today.txt'), 'w') as file:
        file.write(datetime.datetime.today().strftime('%Y-%m-%d'))
    with open(os.path.join(data_dir,'itemlist.csv'), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['product','buy_price','sell_price',])
    with open(os.path.join(data_dir,'bought.csv'), 'w', newline='')as file:
        writer = csv.writer(file)
        writer.writerow(['bought_id','product','buy_date','buy_price','quantity','expiration_date','status'])
    with open(os.path.join(data_dir,'id.txt'), 'w') as file:
        file.write('1')
    with open(os.path.join(data_dir,'sold.csv'), 'w', newline='')as file:
        writer = csv.writer(file)
        writer.writerow(['sell_id','bought_id','product','buy_date','sell_date','buy_price','sell_price','quantity','status'])
    with open(os.path.join(current_directory,'requirements.txt'),'w') as file:
        file.write('requirements:\n'
        'numpy v:1.20.3  \n'
        'rich v:10.2.1 \n'
        'mathplot v:3.4.2 \n'
        '\n')
    with open(os.path.join(current_directory,'readme.txt'), 'w') as file:
        file.write(' usage guide : \n'
        'to use this program start with python main.py -h command so you know the commands that are usable.\n'
        '\n'
        'python main.py inventory  shows the currend inventory and the count of the items there is on the itemlist.\n'
        '\n'
        'with python main.py buy ,products can be bought that are in the itemlist if a product is not in itemlist it can be added.\n'
        "the prices are already in the itemlist so they don't have to be added.\n" 
        'buy  then at prompt in terminal fill in the product you like to add at next prompt in terminal experation date and it is added to buy list.\n'
        '\n'
        'python main.py sell ,removes the given product from the buy list and adds it to the sold list.\n'
        'Give the prompt the product you are selling if it is in the bought list it wil be sold\n'
        '\n'
        'python main.py report ,report gives reports for the date given in the terminal when prompted.\n'
        'Report can give the reports for today\n'
        'yesterday or a given date in the format yyyy-mm-dd\n'
        'Report wil give the data in the terminal and also gives a rich table and a mathplot graph\n'
        '\n'
        'python main.py advance_date ,the date that the program precieves of today can be changed.\n'
        'Just give the number of days You would like to advance'
        'And confirm if it is corect'
        '\n'
        'with python main.py view_itemlist ,the list of avalable products is shown\n'
        '\n'
        'python main.py add_item ,wil ask for the product you want to add, the buy price and sell price\n'
        'and will add it to the item list.'
        '\n'
        'python main.py remove_item ,will give the itemlist and when prompted typ the item to remove it from the item list\n'
        '\n'
        '\n'
        'export will export the info from a argparse given date to a argparse given filename\n'
        '\n'
        'the default for date is the date of today that is in the program\n' 
        'the default for filename is export\n'
        '\n'
        'python main.py export\n'
        'will make a csv file with the name export and the date of today in the program\n'
        '\n'
        'python main.py export -date 2021-05-28 -filename export\n'
        'will make a csv file with the name export with info from the date 2021-05-28\n'
        '\n'
        'python main.py export -date 2025-10-28 -filename export-10-28\n' 
        'will make a csv file with the name export-10-28 with the info from the date 2025-10-28\n') 

def path_exists(map = data_dir):
    file_exists = os.path.exists(map)
    if file_exists:
        None
    else:
        create_files()

#check if path to data  directory exists
path_exists()

#function to check if products in buy are expired (get)
def is_expired():
    date = get.date()
    with open(os.path.join(data_dir,'bought.csv'), 'r') as read_obj:
        reader = csv.DictReader(read_obj)  
        header = reader.fieldnames
        for row in reader:
            if date >= row['expiration_date']:
                row['status'] = 'expired'
                print ('bought_id:'+ row['bought_id'] +'  '+ row['product'] + '  is expired' )
                sell_id = get.id()
                bought_id = row['bought_id']
                product = row['product']
                sell_date = row['expiration_date']
                buy_date = row['buy_date']
                buy_price = row['buy_price']
                sell_price = 0
                quantity = row['quantity']
                status = 'expired'
                new_row = sell_id, bought_id, product,buy_date , sell_date, buy_price, sell_price , quantity, status
                add_line_to_csv('sold.csv',new_row)
                remove_from_csv('bought.csv',bought_id) 

# function to add a line to the bottom of a csv file
def add_line_to_csv(file_name, line_to_add):
    with open(os.path.join(data_dir,file_name), 'a+', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerow(line_to_add)

# function to remove a line by id colomn
def remove_from_csv(file_name, to_remove , colomn='bought_id'):
    is_removed = False
    header = []
    rows_to_keep = []
    rows_to_remove = []
    with open(os.path.join(data_dir,file_name), 'r') as read_obj:
        reader = csv.DictReader(read_obj)
        header = reader.fieldnames
        for row in reader:
            if to_remove != row[colomn]:
                rows_to_keep.append(row)
            elif to_remove == row[colomn]:
                rows_to_remove.append(row)
                is_removed = True
            else:
                print('somthing went wrong!!')
                (exit)
    with open(os.path.join(data_dir,file_name), 'w', newline= '') as new_obj:
        writer = csv.DictWriter(new_obj, fieldnames = header)
        writer.writeheader()
        writer.writerows(rows_to_keep)

    return rows_to_remove

# check if date is iso format (yyyy-mm-dd)
def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError('incorect data format, should be YYYY-MM-DD')

# check if product is in the store
def check_if_exists (to_check, buy = True , file_name='itemlist.csv'):
    is_in_list = False
    with open(os.path.join(data_dir,file_name), 'r') as read_obj:
        reader = csv.DictReader(read_obj)  
        for row in reader:
            if to_check == row['product']:
                is_in_list = True 
    if is_in_list == True and buy == True:
        return
    elif is_in_list == False and buy == False:
        return
    elif is_in_list == True and buy == False:
        print ('product is already on the list')
        exit()
    else:
        option = ''
        print('product is not in the list of products to be sold')
        while option.lower() not in{'yes' , 'no'}:
            option = input ('do you want the product to the list (yes/no)  ')
        if option == 'yes':
            add_item()
            exit()
        else:
            exit()

# check if item is in inventory
def check_in_inventory (to_check, file_name='bought.csv'):
    is_in_list = False
    with open(os.path.join(data_dir,file_name), 'r') as read_obj:
        reader = csv.DictReader(read_obj)  
        for row in reader:
            if to_check == row['product']:
                is_in_list = True 
    if is_in_list:
        return
    else:
        print ('the item is sold out')
        exit()

#functions called by argparse

#add item to list function
def add_item():
    product_to_add = input ('what product do you like to add to the store? ')
    check_if_exists(product_to_add, buy = False)
    buy_price = input('what is the buy price of '+ product_to_add +'? ')
    sell_price = input('what is the sell price of '+ product_to_add +'? ')
    try:
        buy_price = float(buy_price)
        sell_price =float(sell_price)
    except ValueError:
        print('please input a number for the buy and sell price')
        add_item()
    sell_price = float(sell_price)
    buy_price = float(buy_price)
    row = [product_to_add , buy_price , sell_price]
    add_line_to_csv('itemlist.csv',row)


#buy function
def buy():

    product_name = input('what product are you buying?  ')
    check_if_exists(product_name)
    product_id = get.id()
    buy_date = get.date()
    buy_price = get.info('itemlist.csv', product_name, 'buy_price')
    expiration_date= input ('what is the expiration date? (yyyy-mm-dd) ')
    quantity = 1
    validate_date(expiration_date)
    status = 'stored'
    row = [product_id,product_name,buy_date,buy_price,quantity,expiration_date,status]
    #{'id': product_id , 'product': product_name, 'buy date': buy_date, 'buy_price': buy_price, 
    #       'expiration_date': expiration_date, 'status': status}

    add_line_to_csv('bought.csv', row)

    print('thank you for buying  ')       

#sell function
def sell():
    product_name = input('what are you selling?  ')
    check_in_inventory(product_name)
    sell_id = get.id()
    bought_id = get.info('bought.csv', product_name, 'bought_id')
    buy_date = get.info('bought.csv', product_name, 'buy_date')
    sold = remove_from_csv('bought.csv',bought_id)
    sell_date = get.date()
    buy_price = get.info('itemlist.csv', product_name, 'buy_price')
    sell_price = get.info('itemlist.csv', product_name, 'sell_price')
    quantity = 1
    status = 'sold'
    print('you have sold')
    print(sold)
    new_row = (sell_id, bought_id, product_name, buy_date, sell_date,
                buy_price, sell_price , quantity, status)
    add_line_to_csv('sold.csv', new_row)

#time skip function
def advance_date():
    date = get.date()
    begin_date = datetime.datetime.strptime(date,'%Y-%m-%d')
    print('the date is: '+ date)
    days_to_skip = int(input('how many days do you like to advance? (number) '))
    new_date = (begin_date + datetime.timedelta(days_to_skip)).strftime('%Y-%m-%d')
    confirm = ''
    str_new_date = str(new_date)
    while confirm.lower() not in{'yes', 'y' , 'no', 'n'}:
        print( ' the new date is '+ str_new_date)
        confirm = input ('is this OK? (yes/no)  ')
        if confirm == 'yes' or confirm == 'y':
            today = new_date
            with open(os.path.join(data_dir,'today.txt'), 'w') as file:
                file.write (today)
                print('the date is now ' + today)
            exit()
        else:
            exit()

#view items function
def view_items():
    print('here are the items of the store')
    with open(os.path.join(data_dir,'itemlist.csv')) as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)

#remove items from  list function
def remove_item():
    products = ''
    with open(os.path.join(data_dir,'itemlist.csv'), 'r') as read_obj:
        reader = csv.DictReader(read_obj)  
        for row in reader:
            products = products + row['product'] + '\n'
    print (products)
    product_to_remove = input ('what product do you like to remove to the store? ')
    remove_from_csv('itemlist.csv',product_to_remove,'product')
    print(product_to_remove +' is removed from store')

#export data
def to_export():
    date = str(args.date)
    dir = args.filename
    output.export(date,dir)
    

# Parsers:
parser = argparse.ArgumentParser(
        description= 'keep track of the inventory'
        )
subparser = parser.add_subparsers(dest='command', required=True)

#export_parser
today=get.date()
export_parser = subparser.add_parser('export',help=' get buy/sell info for given date in a exported csv file')
export_parser.add_argument('-date',type=datetime.date.fromisoformat, default=today, help='give the date where you want the info for (yyyy,mm,dd) | default = todays date')
export_parser.add_argument('-filename', type=str, default='export', help='give the filename for the export file | default = export')
export_parser.set_defaults(func=to_export)

# view inventory parser
view_inventory_parser = subparser.add_parser('inventory', help='view the inventory')
view_inventory_parser.set_defaults(func=output.view_inventory)
# add buy parser
buy_parser = subparser.add_parser('buy', help='buy products')
buy_parser.set_defaults(func=buy)
# add sell parser
sell_parser = subparser.add_parser('sell', help='sell products')
sell_parser.set_defaults(func=sell)
# add view sales parser
view_sales_parser = subparser.add_parser('report', help=' see the sale reports')
view_sales_parser.set_defaults(func=output.report)
# add advance_time parser:
advance_time_parser = subparser.add_parser('advance_date', help='advance the date')
advance_time_parser.set_defaults(func=advance_date)
# add view itemlist parser
view_itemlist_parser = subparser.add_parser('view_itemlist', help='view the available products')
view_itemlist_parser.set_defaults(func=view_items)
# add  add item to itemlist parser
add_item_parser = subparser.add_parser('add_item', help='add a item to the available products')
add_item_parser.set_defaults(func=add_item)
# add  remove item from from itemlist parser
remove_item_parser = subparser.add_parser('remove_item', help='remove a item from available products')
remove_item_parser.set_defaults(func=remove_item)

args = parser.parse_args()

def main():   

    #check if products are expired
    is_expired()

    #parser function
    args.func()
    
    

if __name__ == '__main__':
    main()


