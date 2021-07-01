import get_data as get
import os
import csv
import datetime
import numpy as np
import matplotlib.pyplot as plt
from rich import print
from rich.console import Console
from rich.table import Table


current_directory = os.getcwd()
data_dir = os.path.join(current_directory,'data')

# check if date is iso format (yyyy-mm-dd)
def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError('incorect data format, should be YYYY-MM-DD')

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

    with open(os.path.join(data_dir,'bought.csv')) as csv_file:
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

    with open(os.path.join(data_dir,'itemlist.csv')) as itemlist:
        itemreader = csv.DictReader(itemlist)
        with open(os.path.join(data_dir,'bought.csv')) as buy:
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

#view report function
def report():
    today = get.date()
    begin_date = datetime.datetime.strptime(today,'%Y-%m-%d')
    yesterday = (begin_date - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    print('for what date do you want the revenue? ')
    date_option = input ('today (t) , yesterday (y),  or date ( yyyy-mm-dd) ')
    if date_option == 't' or date_option == 'today' or date_option == 'vandaag':
        date = today
    elif date_option == 'y' or date_option == 'yesterday' or date_option == 'gisteren':
        date = yesterday
    else:
        date = date_option
        validate_date(date)

    bought_date = get.bought(date)
    sold_date = get.sold(date)
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
    print( 'the revenue of '+ date+ ' is €' + str(round(revenue, 2)))
    print( 'the expences of ' + date+  ' are €' + str(round(buy_prices, 2)))
    print( 'the profit of '+ date+ ' is €' + str(round(profit, 2)))


    # matplot graph
    x = np.array(['bought','sold','expired'])
    y = np.array([int(bought_count),int(sold_count),int(expired_count)])
    plt.subplot(1,2,1)
    plt.bar(x,y)
    plt.title('sales in numbers')

    x = np.array(['revenue','expences','profit'])
    y = np.array([float(revenue),float(buy_prices),float(profit)])
    plt.subplot(1,2,2)
    plt.bar(x,y)
    plt.title('income in euro')
    plt.show()

#export file function

def export(date,dir):
    bought_data = get.bought(date)
    sold_data = get.sold(date)
    print(date)
    print(bought_data)
    print(sold_data)
    header = 'bought_id','sell_id','product','buy_date','sell_date','buy_price','sell_price','quantity','expiration_date','status'
    with open(os.path.join(current_directory,dir+'.csv'), 'w', newline= '') as new_obj:
        writer = csv.DictWriter(new_obj, fieldnames = header, dialect='excel')
        writer.writeheader()
        writer.writerows(bought_data)
        writer.writerows(sold_data)
