from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options
import time


data = pd.read_excel('Workwear brands.xlsx')
websites = data['Domain'].tolist()
weblinks = data['product link'].tolist()

options = webdriver.ChromeOptions()
options.headless = True

dri = webdriver.Chrome('./chromedriver',options=options)

for i in range(len(websites)):
    url = weblinks[i]
    filename = "./parsedData/"+websites[i]
    dri.get(url)

    req_w = dri.execute_script('return document.body.scrollWidth')
    req_h = dri.execute_script('return document.body.scrollHeight')
    time.sleep(20)
    req_h = dri.execute_script('return document.body.scrollHeight')

    html = BeautifulSoup(dri.page_source,'html5lib')
    with open(filename+".txt","w",encoding="utf-8") as f:
        f.write(html.prettify())
    dri.set_window_size(req_w,req_h)
    dri.find_element_by_tag_name('body').screenshot(filename+'.png')

dri.quit()
