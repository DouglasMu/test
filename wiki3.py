from urllib import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host='localhost', port=3306,
                       user='root', passwd='admin',
                       db='wiki', charset='utf8')
cur = conn.cursor()

random.seed(datetime.datetime.now())


def store(title, content):
    cur.execute("INSERT INTO page(title,content) VALUE(\"%s\",\"%s\") ",
                (title, content))
    conn.commit()


def getLinks(url):
    html = urlopen("http://en.wikipedia.org"+url)
    bsObj = BeautifulSoup(html)
    title = bsObj.find("h1").getText()
    content = bsObj.find("div", {"id": "mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsObj.find("div", {"id": "bodyContent"}).\
        findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
links = getLinks("/wiki/Kevin_bacon")
try:
    while len(links)>0:
        newUrl = links[random.randint(0, len(links)-1)].attrs["href"]
        print (newUrl)
        links = getLinks(newUrl)
finally:
    cur.close()
    conn.close()

