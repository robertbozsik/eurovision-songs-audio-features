import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re

# Functions for scraping data of the columns of the Scorecard table
def get_ro(row):
    return row.find('td').text.strip()
    
def get_country(row):
    return row.span.text

def get_contestant(row):
    return row.find_all('a')[1].text.strip()

def get_song(row):
    return row.find_all('div')[3].text.strip()

def get_points(row):
    return row.find_all('td', class_='text-right')[0].text.strip()

def get_place(row):
    return row.find_all('td', class_='text-right')[1].text.strip()

# Functions for scraping the year and the host city from the urls
def get_year(url):
    year_pattern = r'(\d{4})'
    return int(re.findall(year_pattern, url)[0])

def get_host_city(url):
    host_city_pattern = r'([a-z-]*[a-z]+)-'
    host_city = re.findall(host_city_pattern, url)[0]
    host_city = host_city.title()
    return host_city

# Put the scraping functions together and create a dictionary
def create_row(row, url):
    return {'R/O': get_ro(row),
            'Year': get_year(url),
            'Host_City': get_host_city(url),
            'Country': get_country(row),
            'Contestant': get_contestant(row),
            'Song': get_song(row),
            'Points': get_points(row),
            'Place': get_place(row)}

# Get all the URLs from 1956 until 2019
def get_eurovision_urls():
    urls_source = 'https://eurovision.tv/events'
    res = requests.get(urls_source)
    soup = BeautifulSoup(res.content, 'html.parser')
    a_tags1 = soup.find_all('a', class_='text-blue-darkest')[2:18]
    urls1 = [url['href']+'/grand-final' for url in a_tags1]
    a_tags2 = soup.find_all('a', class_='text-blue-darkest')[18:]
    urls2 = [url['href']+'/final' for url in a_tags2]
    urls = urls1 + urls2
    return urls

# A funtion that creates a DataFrame after scraping the URLs
def scrape_eurovision(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    table = soup.body.main.find_all('table', {'class': 'event-table'})[0]
    rows = table.find_all('tr')
    data = [create_row(row, url) for row in rows[1:]] # don't want to get the first row, that is the header
    df_from_data = pd.DataFrame(data)
    return df_from_data


#urls = get_eurovision_urls()
#frames = [scrape_eurovision(url) for url in urls]
#result = pd.concat(frames, ignore_index=True)
#print(result.head())
#print(result.tail())

#result.to_csv('eurovision_per_year.csv', index=False)
#check = pd.read_csv('eurovision_per_year.csv')
#check.head(10)