'''Fetch a web page'''
from requests import get as requests_get
from bs4 import BeautifulSoup 
from json import dump as json_dump
from os import getcwd

# Fetch a web page
p = requests_get('https://github.com/lx-mitin?tab=repositories&q=&type=public')


# Get a list of repositories
soup = BeautifulSoup(p.text,'lxml')
rep_tags = soup.body.find_all('a', itemprop="name codeRepository")
rep_names = [{'rep_name':r.string.strip(),'rep_url':'https://github.com'+r.attrs['href']} for r in rep_tags]

with open(getcwd()+'/data/rep-names.json','w') as json_file:
    json_dump(rep_names,json_file)

print('Repositories data is loaded to `/data/rep-names.json` file')