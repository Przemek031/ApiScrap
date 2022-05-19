from tkinter import *
import requests
import json
import datetime

today=datetime.date.today() 
oneday=datetime.timedelta(days=1) 
yesterday=today-oneday  



url = "https://api.zonda.exchange/rest/trading/orderbook-limited/BTC-PLN/10"
headers = {'content-type': 'application/json'}
responsebtc = requests.request("GET", url, headers=headers)
databtc = responsebtc.json()
pricebtc = (float(databtc['sell'][0]['ra'])+float(databtc['buy'][0]['ra']))/2
pricebtc2 = (float(databtc['sell'][9]['ra'])+float(databtc['buy'][9]['ra']))/2
print(pricebtc,pricebtc2)


responseeur= requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/")
responseeurold= requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/"+str(yesterday))
dataeurold = responseeurold.json()
dataeur = responseeur.json()
priceeurold = dataeurold['rates'][0]['mid']
priceeur = dataeur['rates'][0]['mid']

responseold = requests.get("http://api.nbp.pl/api/cenyzlota/"+str(yesterday))
response = requests.get("http://api.nbp.pl/api/cenyzlota")
dataold = responseold.json()
data = response.json()
priceold=dataold[0]["cena"]
price = data[0]["cena"]

window = Tk()
window.title("Api Scraping Prices")
window.geometry("500x200")
infogold = Label(window, text="Gold Price for 1g (PLN)",font=('Arial', 12, 'bold', 'italic'))
infogold.pack()
pricegold = Label(window,text=price,font=('Arial', 15, 'italic'),foreground='#000000')
pricegold.pack()
infobtc = Label(window, text="BTC Price for 1 (PLN)",font=('Arial', 12, 'bold', 'italic'))
infobtc.pack()
pricebtco = Label(window,text=pricebtc,font=('Arial', 15, 'italic'),foreground='#000000')
pricebtco.pack()
infoeur = Label(window, text="Euro Price for 1 (PLN)",font=('Arial', 12, 'bold', 'italic'))
infoeur.pack()
priceeuro = Label(window,text=priceeur,font=('Arial', 15, 'italic'),foreground='#000000')
priceeuro.pack()
if price > priceold:
    pricegold.config(fg='#00ff00')
else:
    pricegold.config(fg='#ff0000')
if pricebtc > pricebtc2:
    pricebtco.config(fg='#00ff00')
else:
    pricebtco.config(fg='#ff0000')
if priceeur > priceeurold:
    priceeuro.config(fg='#00ff00')
else:
    priceeuro.config(fg='#ff0000')
window.mainloop()




