import requests # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())

ul = tree.findall('//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li')

for li in ul:
    a = li.find('a') # в каждом элементе находим где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка на которую нужно нажать, чтобы перейти на страницу с новостью. (Гиперссылки в html это всегда тэг <a>)
    print(a.text)
    d = li.find('time')
    print(d.get('datetime'))