# coding:utf-8
import urllib
import re

def getHtml(url):
    html = urllib.urlopen(url).read()
#    print(html)
    return html

def getImage(html):
    rex = r'src="(.+?\.jpg)" '
    imgRe = re.compile(rex)
    imgList = imgRe.findall(html)
    return imgList
if __name__ == "__main__":
	urlString = "http://www.ivsky.com"
	html = getHtml(urlString)
	resultList = getImage(html)
	x = 0
	for imgUrl in resultList:
		urllib.urlretrieve(imgUrl,'%s.jpg'%x)
		x += 1


