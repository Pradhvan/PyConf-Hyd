# Request library
import requests


# Using requests library to make a HTTP GET request
# Their are various request method GET , PUT,DELETE

response = requests.get("https://hasjob.co/")

# Check the status code of the request made
# print response.staus_code


# Getting the extracted content
print (response.content)
