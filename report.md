In dit verslag schrijf ik over 3 elementen in mijn superpy opdracht.
1.	 Ik probeer mijn programma zo gebruiksvriendelijk mogelijk te maken door de prompts in input te vragen en te controleren op verschillende inputs.
b.v. bij het aankopen van producten wordt niet alleen gevraagd naar het product naam maar wordt daarna ook gecontroleerd of het product ook daadwerkelijk verkocht wordt.

    def check_if_excists (to_check, buy = True , file_name='itemlist.csv'):
        is_in_list = False
        with open(files_map+'\\'+file_name, 'r') as read_obj:
            reader = csv.DictReader(read_obj)  
            for row in reader:
                if to_check == row['product']:
                   is_in_list = True 
                else:
                    None
  	
Daarbij heb ik ook geprobeerd om de gebruiker invoer zo laag mogelijk te houden door de aankoop en verkoop prijs op te slaan bij het aanmaken van nieuwe producten in de winkel.
Waardoor niet bij elke aan of verkoop de prijs hoeft worden gevraagd.
    
    def add_item():
        product_to_add = input ('what product do u like to add to the store? ')
        check_if_excists(product_to_add, buy = False)
        buy_price   = input('what is the buy price of '+ product_to_add +'? ')
        sell_price = input('what is the sell price of '+ product_to_add +'? ')
        sell_price = float(sell_price)
        buy_price = float(buy_price)



2.	De nodige files en de readme file worden aangemaakt bij het eerste keer uitvoeren van het programma zodat alles op juiste plek aangemaakt wordt en met de juiste indeling.
Daarbij wordt ook gecontroleerd of dat de map al bestaat zodat niet alles wordt overschreven elke keer als het programma geopend wordt.

    def path_exists(map = files_map):
        file_exists = os.path.exists(map)
        if file_exists:
            None
        else:
            create_files()


3. Bij de outputs heb ik geprobeerd om zoveel mogelijk nuttige informatie op een duidelijke manier te presenteren  door  tabellen te gebruiken of door de niet nuttige informatie niet te laten zien 
Bij view_inventory wordt in 1 tabel alles per aankoop laten zien, maar er is ook een duidelijkere tabel met een samenvatting per product waardoor als er snel gekeken moet worden voor nieuwe inkopen, het meteen duidelijk is hoeveel van welk product en wat de eerste houdbaarheidsdatum is van het desbetreffende product is.
 
┏━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ product    ┃ buy date   ┃ buy price ┃ expiration date ┃ status ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ lemon      │ 2021-05-18 │   1.25    │   2021-05-25    │ bought │
│ pear       │ 2021-05-18 │    1.5    │   2021-05-25    │ bought │
│ apple      │ 2021-05-18 │    2.0    │   2021-05-25    │ bought │
│ apple      │ 2021-05-18 │    2.0    │   2021-06-20    │ bought │
│ apple      │ 2021-05-18 │     1     │   2021-06-20    │ bought │
└────────────┴────────────┴───────────┴─────────────────┴────────┘
┏━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ product    ┃ count ┃ first expiration ┃
┡━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ pear       │ 1     │    2021-05-25    │
│ lemon      │ 1     │    2021-05-25    │
│ apple      │ 3     │    2021-05-25    │
│ kiwi       │ 0     │    9999-99-99    │
│ banaan     │ 0     │    9999-99-99    │
│ aardbij    │ 0     │    9999-99-99    │
│ sinasappel │ 0     │    9999-99-99    │
│ ananas     │ 0     │    9999-99-99    │
└────────────┴───────┴──────────────────┘