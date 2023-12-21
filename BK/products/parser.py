import requests
from bs4 import BeautifulSoup
import psycopg2


def get_food():

    urls = 'https://burger-king.by/#burgery-iz-govyadiny'

    r = requests.get(urls)
    food = BeautifulSoup(r.content, "html.parser")

    data = food.find_all("div", {'id': 'burgery-iz-govyadiny'})

    for el in data:
        elem = el.find_all("div", class_="sc-1hg54s1-0 LGqMD")
        for dat in elem:
            cart_url = 'https://burger-king.by' + dat.find("a").get("href")
            yield cart_url


for cart_url in get_food():

    conn = psycopg2.connect(
        host='localhost',
        database='BK',
        user='postgres',
        password='postgres'
    )

    r = requests.get(cart_url)
    food2 = BeautifulSoup(r.content, "html.parser")

    data2 = food2.find('div', class_='sc-6i0h1u-0 lpiHqx')
    name = data2.find('h1', class_="sc-6i0h1u-9 cHOQFA").text
    description = data2.find('p', class_="sc-6i0h1u-15 eSAiEB").text
    weight = data2.find('p', class_="sc-6i0h1u-6 jKxeHJ").text
    price = data2.find('p', class_="sc-6i0h1u-10 eASMOe").text.split('руб.')
    image = data2.find('img', class_="sc-6i0h1u-4 keCigg")['src']
    price = float(price[0])

    cursor = conn.cursor()
    insert_query = f"INSERT INTO products_burger (image, name, description, price, weight) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (image, name, description, price, weight))
    conn.commit()

    # print(name, description, price, weight)



