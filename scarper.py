import requests
import sqlite3
from bs4 import BeautifulSoup

url = 'https://www.technolife.com/category/mobile/mobile-phone'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

conn = sqlite3.connect('products.db')
cursor = conn.cursor()
query = '''CREATE TABLE IF NOT EXISTS products
(id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
price TEXT,
image TEXT,
link TEXT)'''

cursor.execute(query)
conn.commit()

cards = soup.select('section.relative.w-full.rounded-\\[10px\\]')

for card in cards:
    name = card.find('h2').text.strip()
    if name == None:
        continue
    
    price = card.select_one('p.font-semiBold.leading-5').text.strip()
    if price == None:
            continue
    
    image = 'https://www.technolife.com' + card.select_one('a[href^="/product-"] img').get('src')
    
    link = 'https://www.technolife.com' + '' + card.select_one('a[href^="/product-"]').get('href')
    
    query = '''
INSERT INTO products(name, price, image, link)
VALUES(?,?,?,?)
'''

    cursor.execute(query, (name, price, image, link))
    conn.commit()
conn.close()
print('Done')