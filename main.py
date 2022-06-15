from selenium import webdriver
from time import sleep
import urllib.request
import os
from tools import tiktok_download_hashtags
import pickle

browser = webdriver.Chrome()
url = 'https://www.tiktok.com/search?q=shuffle%20dance&t=1655270076317'
browser.get(url)
sleep(20)
tiktoks = browser.find_elements_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div/div')

print(tiktoks)
links = []
n = 0
for tiktok in tiktoks:
    print(n)
    a_element = tiktok.find_elements_by_css_selector("a")
    if len(a_element) > 0:
        links.append(a_element[0].get_attribute("href"))
    n += 1

for i in range(len(links)):
    try:
        browser.get(links[i])
        tiktok_download_hashtags(browser=browser, links=links, i=i)
        sleep(3)
    except:
        pass


print("!FINISH!"*10)
sleep(1000)
browser.close()