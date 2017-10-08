import requests

import pandas as pd

from selenium import webdriver

import time

from selenium.webdriver.common import keys

from bs4 import BeautifulSoup as BS

browser = webdriver.Firefox()

browser.get('https://auth.hasgeek.com/login')

time.sleep(2)

icon = browser.find_element_by_xpath('//*[@id="showmore"]')

icon.click()

time.sleep(2)

email = browser.find_elements_by_xpath('//*[@id="username"]')

email[0].send_keys('Pradhvanbisht@gmail.com')

password = browser.find_element_by_xpath('//*[@id="password"]')

with open('test.txt', 'r') as myfile:  # Reads password from a text file
    Password = myfile.read().replace('\n', '')

password.send_keys(Password)

LOG = browser.find_elements_by_xpath(
    '//*[@id="passwordlogin"]/div[3]/div/button')

LOG[0].click()

time.sleep(3)

browser.get('https://hasjob.co/')

time.sleep(10)

# Scrolls down to the end of the page

lenOfPage = browser.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while(match == False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match = True

time.sleep(4)

pageSource = browser.page_source

soup = BS(pageSource.content, 'html.parser')

base_url = 'https://hasjob.co'+

city = soup.find_all('span', {'class': 'annotation top-left'})
date = soup.find_all('span', {'class': 'annotation top-right'})
title = soup.find_all('span', {'class': 'headline'})
company = soup.find_all('span', {'class': 'annotation bottom-right'})
links = soup.find_all('a', {'class': 'stickie'})

city_list = []

post_date = []

job_title = []

name_company = []

job_links = []


for i in city:
    city_list.append(i.get_text())

for i in date:
    post_date.append(i.get_text())

for i in title:
    job_title.append(i.get_text())

for i in company:
    name_company.append(i.get_text())

for i in links:
    job_links.append(base_url + i.get('href'))

percentile_list = pd.DataFrame(
    {'City': city_list,
     'Date': post_date,
     'Job': job_title,
     'Company': name_company,
     'URL': job_links
     })

 df = pd.DataFrame(percentile_list)

df.to_csv("new.csv", header=True)
