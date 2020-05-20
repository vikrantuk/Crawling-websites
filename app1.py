from selenium import webdriver
from bs4 import BeautifulSoup

url = 'http://www.google.com'
dri = webdriver.Chrome('./chromedriver')
dri.get(url)
filename = "./parsedData/"+dri.title
html = BeautifulSoup(dri.page_source,'html5lib')
with open(filename+".txt","w",encoding="utf-8") as f:
    f.write(html.prettify())
dri.save_screenshot(filename+'.png')
dri.close()
