import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

URL = 'https://www.carwale.com/maruti-suzuki-cars/'

page = requests.get(URL)

page.status_code

htmlCode = page.text
soup = BeautifulSoup(htmlCode)

htmlCode

content = soup.find('div', attrs={'id' :'root'})
print(content)
t = content.text
print(t)

content = soup.find('div', attrs={'class' : 'root'})
t = t.strip("\n")
print(t)

content = soup.find('div', attrs={'class' : 'o-cE o-dH o-c8 o-db o-bO o-ck o-C'})
#print(content)
tt = content.text
r1 = tt.split("\n")
print(r1)
cars = []
# A sample pattern you might expect (update if needed)
for row in soup.select("table tr"):
    cols = row.find_all('td')
    if len(cols) >= 2:
        car_name = cols[0].get_text(strip=True)
        price = cols[1].get_text(strip=True)
        cars.append((car_name, price))
cars1 = []
for x in cars:
  if x[1].startswith("Rs"):
    cars1.append(x)
  
# Print the result
print("Car Name and Prices:")
for name, price in cars1:
    print(f"{name} - {price}")

#print(f"{name} - {price}")
print("Car Name and Prices:")
for name, price in cars1:
    print(f"{name} - {price}")

#CREATE A DATAFRAME AND SAVE IT IN CSV FILE
df = pd.DataFrame(cars1, columns=["Car Name", "Price"])
print(df)
'''
df.to_excel('output.xlsx',index=False)
from os import files
files.download('output.xlsx')
'''
'''
datatoexcel = pd.ExcelWriter('CarsData1.xlsx')
df.to_excel(datatoexcel)
datatoexcel.close()
print(datatoexcel)
'''
'''
file_name = 'carsdata.xlsx'
df.to_excel(file_name)
'''
df.to_excel('carsdata.xlsx',header=True,index=True)
import os
os.startfile("carsdata.xlsx")
