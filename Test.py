from bs4 import BeautifulSoup
import urllib

url = "http://bj.58.com/pingbandiannaos/26062681492781x.shtml"

wb_data = urllib.urlopen(url)
soup = BeautifulSoup(wb_data)

title = soup.title.text
print title
price = soup.select('#content span.price')
date = soup.select('.time')
area = soup.select('.c_25d')

for i in price:
    print i
for j in date:
    print j
for k in area:
    print k