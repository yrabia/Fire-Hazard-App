from urllib.request import urlopen
import sqlite3
import csv

import requests
from bs4 import BeautifulSoup
from kivy.app import App
from kivy.uix.widget import Widget
from pip._internal import req

url = "https://www.fire.ca.gov/incidents/"

uClient = urlopen(url)  # opening up connection grabbing the page
page_html = uClient.read()
uClient.close()
page_soup = BeautifulSoup(page_html, "html.parser")  # html parsing
containers = page_soup.findAll("div", {"class": "featured-incident esri-link-from-popup"})  # grabs each event
container = containers[0]
print(container.div)

filename = "products.csv"
f = open(filename, "w")

headers = "latitude, longitude \n"

f.write(headers)

for container in containers:
    lat = container["data-lat"]
    long = container["data-long"]

    f.write(lat + "," + long + "\n")
f.close()

conn = sqlite3.connect('mapvalues.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS mapvalues')
cur.execute('''
CREATE TABLE "mapvalues"(
    "latitude" TEXT,
    "longitude" TEXT
)
''')

fname = 'products.csv'

with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        latitude=row[0]
        longitude=row[1]
        cur.execute('''INSERT INTO mapvalues(latitude,longitude)
        VALUES (?,?)''',(latitude, longitude))
        conn.commit()
