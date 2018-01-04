from bs4 import BeautifulSoup
import urllib
import re
def getHtml(url):
    html = urllib.urlopen(url)
    return html

def getImg(html):
    bsObj = BeautifulSoup(html)
    imgList = bsObj.findAll("img")
    print imgList
    #imgList = imgList1.findAll(r'src="(.+?\.jpg)" ')
    return imgList
if __name__ == "__main__":
    x = 0
    #local = "E:\\PythonFile\\test\\image"
    for i in range(1, 20):
	    url = ("http://www.ivsky.com/tupian/renwutupian/index_%s.html"%i)
	    html = getHtml(url)
	    resultList = getImg(html)
	    for imgUrl in resultList:
		    urllib.urlretrieve(imgUrl.get("src"),'%s.jpg'%x)
		    x += 1

