 usage guide : 
dependeties:
numpy v:1.20.3  
rich v:10.2.1 
mathplot v:3.4.2 

to use this program start with python main.py -h command so you know the commands that are usable.

python main.py inventory  shows the currend inventory and the count of the items there is on the itemlist.

with python main.py buy ,products can be bought that are in the itemlist if a product is not in itemlist it can be added.
the prices are already in the itemlist so they don't have to be added.
buy  then at prompt in terminal fill in the product you like to add at next prompt in terminal experation date and it is added to buy list.

python main.py sell ,removes the given product from the buy list and adds it to the sold list.
Give the prompt the product you are selling if it is in the bought list it wil be sold

python main.py report ,report gives reports for the date given in the terminal when prompted.
Report can give the reports for today
yesterday or a given date in the format yyyy-mm-dd
Report wil give the data in the terminal and also gives a rich table and a mathplot graph

python main.py advance_date ,the date that the program precieves of today can be changed.
Just give the number of days You would like to advanceAnd confirm if it is corect
with python main.py view_itemlist ,the list of avalable products is shown

python main.py add_item ,wil ask for the product you want to add, the buy price and sell price
and will add it to the item list.
python main.py remove_item ,will give the itemlist and when prompted typ the item to remove it from the item list


export will export the info from a argparse given date to a argparse given filename

the default for date is the date of today that is in the program
the default for filename is export

python main.py export
will make a csv file with the name export and the date of today in the program

python main.py export -date 2021-05-28 -filename export
will make a csv file with the name export with info from the date 2021-05-28

python main.py export -date 2025-10-28 -filename export-10-28
will make a csv file with the name export-10-28 with the info from the date 2025-10-28
