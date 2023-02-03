from urllib.request import urlopen
import sqlite3
import csv
import csv_to_sqlite

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

headers = "latitude, longitude, contained, name, website \n"

f.write(headers)


def listToString(s):
    strl = " "

    for ele in s:
        strl += ele
    return strl


for container in containers:
    lat = container["data-lat"]
    long = container["data-long"]
    contained = ([item.get_text(strip=True) for item in container.select("span.incident-contained")])
    p_contained = listToString(contained)
    name = ([item.get_text(strip=True) for item in container.select("div.incident-label")])
    the_name = listToString(name)
    website = "https://www.fire.ca.gov/incidents/"

    f.write(lat + "," + long + "," + p_contained + "," + the_name + "," + website + "\n")

f.close()
