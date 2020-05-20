from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

data = pd.read_excel('Workwear brands.xlsx')
websites = data['Domain'].tolist()
weblinks = data['product link'].tolist()

dri = webdriver.Chrome('./chromedriver')

for i in range(len(websites)):
    url = weblinks[i]
    filename = "./parsedData/"+websites[i]
    dri.get(url)
    
    html = BeautifulSoup(dri.page_source,'html5lib')
    with open(filename+".txt","w",encoding="utf-8") as f:
        f.write(html.prettify())
    dri.save_screenshot(filename+'.png')
dri.close()
