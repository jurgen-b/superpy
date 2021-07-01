import os
import csv

current_directory = os.getcwd()
data_dir = os.path.join(current_directory,'data')

# all functions to get specified data for main.py

#function to get a id number
def id():
    with open(os.path.join(data_dir,'id.txt'),'r') as read:
        for line in read:
            if line:
                product_id = line.split()[0]
                new_id = int(product_id) +1
                new_product_id = str(new_id)
                with open(os.path.join(data_dir,'id.txt'),'w') as w:
                    w.write(new_product_id)
                    return product_id

#function to get the reports
def bought(date):
    data = []
    with open(os.path.join(data_dir,'bought.csv'), 'r') as read_obj:
        reader = csv.DictReader(read_obj)  
        for row in reader:
            if date == row['buy_date']:
                data.append(row)
    return data

def sold(date):
    data = []
    with open(os.path.join(data_dir,'sold.csv'), 'r') as read_obj:
        reader = csv.DictReader(read_obj)
        for row in reader:
            if date == row['sell_date']:
                data.append(row)
    return data

# function to get date out of the file
def date():
    with open(os.path.join(data_dir,'today.txt'),'r') as read:
        for line in read:
            return line

#function to find specified info of product in the csv file
def info(file_name, product, tofind):
    with open(os.path.join(data_dir,file_name), 'r') as read_obj:
        reader = csv.DictReader(read_obj)  
        for row in reader:
            if product == row['product']:
                found = row[tofind]
                return found