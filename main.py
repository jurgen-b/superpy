
# Imports
import argparse
import csv
import datetime
import os
from rich import print
from rich.console import Console
from rich.table import Table
import numpy as np
import matplotlib.pyplot as plt

# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'
# Your code below this line.

# make the export function 

def main():

    current_directory = os.getcwd()
    files_map = os.path.join(current_directory,'files')
        # Store current date variable:
    now = datetime.datetime.now()

    # Function to create a directory with the files needed for functions if not present.
    # if present get products and date from files !!

    def create_files():
        os.mkdir(files_map)
        today_txt=os.path.join(files_map,'today.txt')
        with open(os.path.join(today_txt), 'w') as file:
            file.write(datetime.datetime.today().strftime('%Y-%m-%d'))
        with open(os.path.join(files_map,'itemlist.csv'), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['product','buy_price','sell_price',])
        with open(os.path.join(files_map,'buy.csv'), 'w', newline='')as file:
            writer = csv.writer(file)
            writer.writerow(['bought_id','product','buy_date','buy_price','quantity','expiration_date','status'])
        with open(os.path.join(files_map,'id.txt'), 'w') as file:
            file.write('1')
        with open(os.path.join(files_map,'sold.csv'), 'w', newline='')as file:
            writer = csv.writer(file)
            writer.writerow(['sell_id','bought_id','product','buy_date','sell_date','buy_price','sell_price','quantity','status'])
        with open(os.path.join(current_directory,'readme.txt'), 'w') as file:
            file.write(' usage guide : \n'
            'dependeties:\n'
            'numpy v:1.20.3  \n'
            'rich v:10.2.1 \n'
            'mathplot v:3.4.2 \n'
            '\n'
            'to use this program start with -h command so u know the commands that are usable.\n'
            'inventory  shows the currend inventory and the count of the items there is on the itemlist.\n'
            '\n'
            'with python main.py buy ,products can be bought that are in the itemlist if a product is not in itemlist it can be added.\n'
            "the prices are already in the itemlist so they don't have to be added.\n" 
            'buy  then at prompt in terminal fill in the product u like to add at next prompt in terminal experation date and it is added to buy list.\n'
            '\n'
            ' python main.py sell ,removes the given product from the buy list and adds it to the sell list.\n'
            '\n'
            ' python main.py report ,report gives reports for the date given in the terminal when prompted.\n'
            '\n'
            ' python main.py advance_date ,the date that the program precieves of today can be changed.\n'
            '\n'
            'with python main.py view_itemlist ,the list of avalable products is shown\n'
            '\n'
            'python main.py add_item ,wil ask for the product u want to add, the buy price and sell price.\n'
            '\n'
            'python main.py remove_item ,will give the itemlist and when prompted typ the item to remove it from the avalable list\n'
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


    def path_exists(map = files_map):
        file_exists = os.path.exists(map)
        if file_exists:
            None
        else:
            create_files()
    path_exists()

    #all functions needed

    #check if items in buy are expired
    def is_expired():
        date = get_date()
        with open(os.path.join(files_map,'buy.csv'), 'r') as read_obj:
            reader = csv.DictReader(read_obj)  
            header = reader.fieldnames
            for row in reader:
                if date >= row['expiration_date']:
                   row['status'] = 'expired'
                   print ('bought_id:'+ row['bought_id'] +'  '+ row['product'] + '  is expired' )
                   sell_id = get_id()
                   bought_id = row['bought_id']
                   product = row['product']
                   sell_date = row['expiration_date']
                   buy_date = row['buy_date']
                   buy_price = row['buy_price']
                   sell_price = 0
                   quantity = row['quantity']
                   status = 'expired'
                   new_row = sell_id, bought_id, product,buy_date , sell_date, buy_price, sell_price , quantity, status
                   add_to_csv('sold.csv',new_row)
                   remove_from_csv('buy.csv',bought_id) 
                else:
                    None

    # function to add lines to csv file
    def add_to_csv(file_name, line_to_add):
        with open(os.path.join(files_map,file_name), 'a+', newline='') as write_obj:
            csv_writer = csv.writer(write_obj)
            csv_writer.writerow(line_to_add)

    # function to remove a line by id colomn
    def remove_from_csv(file_name, to_remove , colomn='bought_id'):
        is_removed = False
        header = []
        rows_to_keep = []
        rows_to_remove = []
        with open(os.path.join(files_map,file_name), 'r') as read_obj:
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
        with open(os.path.join(files_map,file_name), 'w', newline= '') as new_obj:
            writer = csv.DictWriter(new_obj, fieldnames = header)
            writer.writeheader()
            writer.writerows(rows_to_keep)

        return rows_to_remove
    
    # function to get date out of the file
    def get_date():
        with open(os.path.join(files_map,'today.txt'),'r') as read:
            for line in read:
                return line
    
    #function to make a id number
    def get_id():
        with open(os.path.join(files_map,'id.txt'),'r') as read:
            for line in read:
                if line:
                    product_id = line.split()[0]
                    new_id = int(product_id) +1
                    new_product_id = str(new_id)
                    with open(files_map+'\\id.txt','w') as w:
                        w.write(new_product_id)
                        return product_id
    
    #function to find id number of product
    def find_id(file_name, product):
        with open(os.path.join(files_map,file_name), 'r') as read_obj:
            reader = csv.DictReader(read_obj)  
            for row in reader:
                if product == row['product']:
                    product_id = row['bought_id']
                    return product_id

    #function to get the reports
    def get_bought(date):
        data = []
        with open(os.path.join(files_map,'buy.csv'), 'r') as read_obj:
            reader = csv.DictReader(read_obj)  
            for row in reader:
                if date == row['buy_date']:
                    data.append(row)
        return data
    
    def get_sold(date):
        data = []
        with open(os.path.join(files_map,'sold.csv'), 'r') as read:
            reader2 = csv.DictReader(read)
            for row in reader2:
                if date == row['sell_date']:
                    data.append(row)
        return data

    # check if date is iso format (yyyy-mm-dd)
    def validate_date(date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            raise ValueError('incorect data format, shoud be YYYY-MM-DD')

    # check if product is in the store
    def check_if_excists (to_check, buy = True , file_name='itemlist.csv'):
        is_in_list = False
        with open(os.path.join(files_map,file_name), 'r') as read_obj:
            reader = csv.DictReader(read_obj)  
            for row in reader:
                if to_check == row['product']:
                   is_in_list = True 
                else:
                    None
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
                option = input ('do u want the product to the list (yes/no)  ')
            if option == 'yes':
                add_item()
                exit()
            else:
                exit()

    # check if item is in inventory
    def check_in_inventory (to_check, file_name='buy.csv'):
        is_in_list = False
        with open(os.path.join(files_map,file_name), 'r') as read_obj:
            reader = csv.DictReader(read_obj)  
            for row in reader:
                if to_check == row['product']:
                   is_in_list = True 
                else:
                    None
        if is_in_list:
            return
        else:
            print ('the item is sold out')
            exit()

    # get buy/sell price
    def get_price(product, buy_or_sell):
        with open(os.path.join(files_map,'itemlist.csv')) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                if product == line['product']:
                    price = line[buy_or_sell]
                    return price

    #check if products are expired
    is_expired()

    # all argparce functions

    #view inventory function
    def view_inventory():
        to_add = ''
        add_product = ''
        add_count = ''

        table = Table(show_header=True, header_style='bold red')
        table.add_column('product', style='dim', width=10)
        table.add_column('buy date')
        table.add_column('buy price', justify='center')
        table.add_column('expiration date', justify='center')
        table.add_column('status')

        with open(os.path.join(files_map,'buy.csv')) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for lines in csv_reader:
                product = lines['product']
                date = lines ['buy_date']
                buy_price = lines['buy_price']
                status = lines['status']
                expiration_date = lines['expiration_date']
                table.add_row(
                product ,date,buy_price, expiration_date ,status
                )

        table2 = Table(show_header=True, header_style='bold red')
        table2.add_column('product', style='dim', width=10)
        table2.add_column('count')
        table2.add_column('first expiration', justify='center')

        with open(os.path.join(files_map,'itemlist.csv')) as itemlist:
            itemreader = csv.DictReader(itemlist)
            with open(os.path.join(files_map,'buy.csv')) as buy:
                buyreader = csv.DictReader(buy)
                for items in itemreader:
                    count = 0
                    exdate = '9999-99-99'
                    buy.seek(0)
                    for lines in buyreader:
                        add_product = items['product']
                        if items['product'] == lines ['product']:
                            count = count +1
                            if exdate >= lines['expiration_date']:
                                exdate = lines['expiration_date']
                    add_count = str(count)
                    to_add = add_product,add_count,exdate
                    table2.add_row(add_product,add_count,exdate)

        print(table)
        print(table2)
    
    #buy function
    def buy():

        product_name = input('what product are u buying?  ')
        check_if_excists(product_name)
        product_id = get_id()
        buy_date = get_date()
        buy_price = get_price(product_name, 'buy_price')
        expiration_date= input ('what is the expiration date? (yyyy-mm-dd) ')
        quantity = 1
        validate_date(expiration_date)
        status = 'stored'
        row = [product_id,product_name,buy_date,buy_price,quantity,expiration_date,status]
        #{'id': product_id , 'product': product_name, 'buy date': buy_date, 'buy_price': buy_price, 
        #       'expiration_date': expiration_date, 'status': status}

        add_to_csv('buy.csv', row)

        print('thank u for buying  ')       

    #sell function
    def sell():
        product_name = input('what are u selling?  ')
        check_in_inventory(product_name)
        sell_id = get_id()
        bought_id = find_id('buy.csv', product_name)
        sold = remove_from_csv('buy.csv',bought_id)
        sell_date = get_date()
        buy_price = get_price( product_name, 'buy_price')
        sell_price = get_price( product_name, 'sell_price')
        quantity = 1
        status = 'sold'
        print('you have sold')
        print(sold)
        #sold.status = 'sold'
        new_row = sell_id, bought_id, product_name, sell_date, buy_price, sell_price , quantity, status
        add_to_csv('sold.csv', new_row)

    #view report function
    def report():
        date_option = ''
        today = get_date()
        yesterday = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%Y-%m-%d')
        print (today +','+ yesterday)
        print('for what date do u want the revenue? ')
        date_option = input ('today (t) , yesterday (y),  or date ( yyyy-mm-dd) ')
        if date_option == 't' or date_option == 'today' or date_option == 'vandaag':
            date = today
        elif date_option == 'y' or date_option == 'yesterday' or date_option == 'gisteren':
            date = yesterday
        else:
            date = date_option
            validate_date(date)

        bought_date = get_bought(date)
        sold_date = get_sold(date)
        sell_prices = 0.0
        buy_prices = 0.0
        sold_count = 0
        expired_count = 0
        bought_count = 0

        for lines in bought_date:
            bought_count = bought_count +1
            quantity = int(lines['quantity'])
            t_buy_price = float(lines['buy_price'])
            buy_prices = buy_prices + t_buy_price * quantity
        
        for lines in sold_date:
            quantity = int(lines['quantity'])
            t_buy_price = float(lines['buy_price'])
            buy_prices = buy_prices + t_buy_price * quantity
            t_sell_price = float(lines['sell_price'])
            sell_prices = sell_prices + t_sell_price * quantity
            if lines['status'] == 'sold':
                sold_count = sold_count + 1
            elif lines['status'] == 'expired':
                expired_count = expired_count + 1
            
        # rich

        table = Table(show_header=True, header_style='bold red')
        table.add_column('product', style='dim', width=10)
        table.add_column('buy or sell date')
        table.add_column('buy price', justify='right')
        table.add_column('sell price', justify='right')
        table.add_column('status')


        for lines in bought_date:
            product = lines['product']
            date = lines['buy_date']
            buy_price = lines['buy_price']
            sell_price = '0'
            status = lines['status']
            table.add_row(
            product , date, buy_price , sell_price , status
                )
        
        for lines in sold_date:
            product = lines['product']
            date = lines ['sell_date']
            buy_price = lines['buy_price']
            sell_price = lines['sell_price']
            status = lines['status']
            table.add_row(
                product ,date,buy_price, sell_price , status
            )

        print(table)

        revenue = sell_prices
        profit  = sell_prices - buy_prices
        print( 'total sold today = '+ str(sold_count))
        print( 'total expired today = '+ str(expired_count))
        print( 'total bought today = '+ str(bought_count))
        print( 'the revenue of '+ date+ ' is €' + str(revenue))
        print( 'the expences of ' + date+  ' are €' + str(buy_prices))
        print( 'the profit of '+ date+ ' is €' + str(profit))


        # matplot graph
        x = np.array(['bought','sold','expired'])
        y = np.array([int(bought_count),int(sold_count),int(expired_count)])
        plt.subplot(1,2,1)
        plt.bar(x,y)
        plt.title('sales in numbers')

        x = np.array(['revenue','expences','profit'])
        y = np.array([int(revenue),int(buy_prices),int(profit)])
        plt.subplot(1,2,2)
        plt.bar(x,y)
        plt.title('income in euro')
        plt.show()

    #time skip function
    def advance_time():
        date = get_date()
        begin_date = datetime.datetime.strptime(date,'%Y-%m-%d')
        print('the date is: '+ date)
        days_to_skip = int(input('how many days do u like to advance? (number)'))
        new_date = (begin_date + datetime.timedelta(days_to_skip)).strftime('%Y-%m-%d')
        confirm = ''
        str_new_date = str(new_date)
        while confirm.lower() not in{'yes', 'y' , 'no', 'n'}:
            print( ' the new date is '+ str_new_date)
            confirm = input ('is this oke? (yes/no)  ')
            if confirm == 'yes' or confirm == 'y':
                today = new_date
                with open(now.strftime(files_map+'\\today')+'.txt', 'w') as file:
                    file.write (today)
                exit()
            else:
                exit()
    
    #view items function
    def view_items():
        print('here are the items of the store')
        with open(os.path.join(files_map,'itemlist.csv')) as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                print(line)

    #add item to list function
    def add_item():
        product_to_add = input ('what product do u like to add to the store? ')
        check_if_excists(product_to_add, buy = False)
        buy_price   = input('what is the buy price of '+ product_to_add +'? ')
        sell_price = input('what is the sell price of '+ product_to_add +'? ')
        sell_price = float(sell_price)
        buy_price = float(buy_price)
        row = [product_to_add , buy_price , sell_price]
        add_to_csv('itemlist.csv',row)

    #remove items from  list function
    def remove_item():
        products = ''
        with open(os.path.join(files_map,'itemlist.csv'), 'r') as read_obj:
            reader = csv.DictReader(read_obj)  
            for row in reader:
                products = products + row['product'] + '\n'
        print (products)
        product_to_remove = input ('what product do u like to remove to the store? ')
        remove_from_csv('itemlist.csv',product_to_remove,'product')
        print(product_to_remove +' is removed from store')
    
    #export data
    def export():
        date = str(args.date)
        bought_data = get_bought(date)
        sold_data = get_sold(date)

        print(bought_data)
        print(sold_data)
        header = 'bought_id','sell_id','product','buy_date','sell_date','buy_price','sell_price','quantity','expiration_date','status'
        with open(os.path.join(current_directory,args.filename+'.csv'), 'w', newline= '') as new_obj:
            writer = csv.DictWriter(new_obj, fieldnames = header, dialect='excel')
            writer.writeheader()
            writer.writerows(bought_data)
            writer.writerows(sold_data)
    
    # Parsers:
    parser = argparse.ArgumentParser(
            description= 'keep track of the inventory'
            )
    subparser = parser.add_subparsers(dest='command', required=True)
    #export_parser
    today=get_date()
    export_parser = subparser.add_parser('export',help=' get buy/sell info for given date in a exported csv file')
    export_parser.add_argument('-date',type=datetime.date.fromisoformat, default=today, help='give the date where u want the info for (yyyy,mm,dd) | default = todays date')
    export_parser.add_argument('-filename', type=str, default='export', help='give the filename for the export file | default = export')

    export_parser.set_defaults(func=export)
  
    # view inventory parser
    view_inventory_parser = subparser.add_parser('inventory', help='view the inventory')
    view_inventory_parser.set_defaults(func=view_inventory)
    # add buy parser
    buy_parser = subparser.add_parser('buy', help='buy products')
    buy_parser.set_defaults(func=buy)
    # add sell parser
    sell_parser = subparser.add_parser('sell', help='sell products')
    sell_parser.set_defaults(func=sell)
    # add view sales parser
    view_sales_parser = subparser.add_parser('report', help=' see the sale reports')
    view_sales_parser.set_defaults(func=report)
    # add advance_time parser:
    advance_time_parser = subparser.add_parser('advance_date', help='advance the date')
    advance_time_parser.set_defaults(func=advance_time)
    # add view itemlist parser
    view_itemlist_parser = subparser.add_parser('view_itemlist', help='view the available products')
    view_itemlist_parser.set_defaults(func=view_items)
    # add  add item to itemlist parser
    add_item_parser = subparser.add_parser('add_item', help='add a item to the available products')
    add_item_parser.set_defaults(func=add_item)
    # add  remove item from from itemlist parser
    remove_item_parser = subparser.add_parser('remove_item', help='remove a item from available products')
    remove_item_parser.set_defaults(func=remove_item)

    #making the function run
    args = parser.parse_args()
    args.func()
    
    

if __name__ == '__main__':
    main()