import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

def extract_data(item):	
    data = []
    title = item.find('div','product-card__title').text.strip()
    subTitle = item.find('div','product-card__subtitle').text.strip()
    price = item.find('div','product-price__wrapper css-9xqpgk').text.strip()
    url2 = item.find('a','product-card__link-overlay').get('href')
    ####
    try:
        data = requests.get(url2)
        soup2 = BeautifulSoup(data.text, 'html.parser')
        image = soup2.find('img', class_='css-viwop1 u-full-width u-full-height css-m5dkrx').get('src')	
    except Exception as e:
        print(e)
        image = "Not Found"
    result = {"title":title, "subtitle":subTitle, "price":price, "image":[image]}
    return result
def search(url):
    result = []
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text,"html.parser")
    soap_result = soup.find_all("div",class_="product-card__body")
    for item in soap_result:
        record = extract_data(item)
        result.append(record)
    return result
data = search("https://www.nike.com/w/mens-shoes-nik1zy7ok")
if data:
    print("Almost Completed")
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
