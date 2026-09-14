from bs4 import BeautifulSoup
import requests


with open('test.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# h1 = soup.find('div', class_ = "product").text
# print(h1)

div = soup.find('div', class_ = 'product')
link = div.find('a')['href']
print(link)
