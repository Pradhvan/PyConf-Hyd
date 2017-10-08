# Request library
import requests

import os

import pandas as pd

#from pandas import DataFrame

# Parser for sructuring the unstructured data
from bs4 import BeautifulSoup

#import numpy as np
# Using requests library to make a HTTP GET request
# Their are various request method GET,PUT,DELETE

response = requests.get("https://hasjob.co/")

# Check the status code of the request made
# print response.staus_code

#import csv

# Printing the extracted content
# print (response.content)


# Creating a soup object
soup = BeautifulSoup(response.content, 'html.parser')

# Structring the content in human readable form
# print (soup.prettify())

# Creating an unordered list by analyzing the web page for new jobs list
# ul_lists = soup.find_all('ul')


# Finding the unordered list that contains the only the job section
# One way of doing it
# ul_lists[-1]

# Using the find all function and finding the list of job

base_url = 'https://hasjob.co'
city = soup.find_all('span', {'class': 'annotation top-left'})
date = soup.find_all('span', {'class': 'annotation top-right'})
title = soup.find_all('span', {'class': 'headline'})
company = soup.find_all('span', {'class': 'annotation bottom-right'})
links = soup.find_all('a',{'class':'stickie'})


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
    job_links.append( base_url + i.get('href'))

#percentile_list = pd.DataFrame(np.column_stack([city_list, post_date, job_title, name_company]),
#                               columns=['lst1tite', 'lst2itie', 'lst3tite', 'name'])


percentile_list = pd.DataFrame(
    {'City': city_list,
     'Date': post_date,
     'Job': job_title,
     'Company': name_company,
     'URL':job_links
     })

df = pd.DataFrame(percentile_list)

df.to_csv("new.csv", header = True)

#print(df)
# with open("jobs.csv", "w") as f:
#    wr = csv.writer(f, delimiter = '\n')
#    wr.writerow(city_list)
