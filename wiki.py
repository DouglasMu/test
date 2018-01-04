from urllib import urlopen
from bs4 import BeautifulSoup
import re
def getWeb(url):
    html = urlopen(url)
    #html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a", {"href": re.compile("http://.*?")}):
        print link.get("href")
        return link.get("href")
if __name__ == "__main__":
    url = "http://en.wikipedia.org/wiki/Kevin_Bacon"
    #getWeb(url)
    while 1:
        newurl = getWeb(url)
        getWeb(newurl)

