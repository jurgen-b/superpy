 usage guide : 
 dependeties:
 numpy v:1.20.3
 rich v:10.2.1
 mathplot v:3.4.2

to use this program start with -h command so u know the commands that are usable.

all commands are given in terminal with python main.py command

inventory  shows the currend inventory and the count of the items there is on the itemlist.

with the buy command products can be bought that are in the itemlist if a product is not in itemlist it can be added.
the prices are already in the itemlist so they don't have to be added.
buy  then at prompt in terminal fill in the product u like to add at next prompt in terminal experation date and it is added to buy list.

 the sell command removes the given product from the buy list and adds it to the sell list.

 report gives reports for the date given in the terminal when prompted.

 with advance date the date that the program precieves of today can be changed.

with the view_itemlist command the list of avalable products is shown

add_item  wil ask for the product u want to add, the buy price and sell price.

remove_item will give the itemlist and when prompted typ the item to remove it from the avalable list

export will export the info from a argparse given date to a argparse given filename

    the default for date is the date of today that is in the program 
    the default for filename is export

    python main.py export
    will make a csv file with the name export and the date of today in the program

    python main.py export -date 2021-05-28 -filename export
    will make a csv file with the name export with info from the date 2021-05-28

    python main.py export -date 2025-10-28 -filename export-10-28
    will make a csv file with the name export-10-28 with the info from the date 2025-10-28

