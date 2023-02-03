import sqlite3, csv

connection = sqlite3.connect("dataformap.db")
cursor = connection.cursor()

with open('products.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO DataForMap VALUES (?,?,?,?,?)", row.split(","))
        connection.commit()
        no_records += 1
connection.close()
print('\n{} Records Transferred'.format(no_records))
