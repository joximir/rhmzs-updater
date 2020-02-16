#!/usr/bin/env python

import urllib.request as url    #grabbing HTML
from bs4 import BeautifulSoup   #getting data out of HTML (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
from pathlib import Path        #file manipulation  

#get web page 
PISMO_LATINICA = False
if PISMO_LATINICA :
    page = url.urlopen('http://www.hidmet.gov.rs/latin/osmotreni/index.php')
else:
    page = url.urlopen('http://www.hidmet.gov.rs/ciril/osmotreni/index.php')


#get weather info from page
soup = BeautifulSoup(page, features='html.parser')

# for tr in soup.table.find_all('tr') if true:

prognoza = list()

found = False
for td in soup.findAll('td', {'class':['bela75', 'siva75']}):
    if found:
        temp = td.string
        found = False
        prognoza.append((grad, temp))
        continue
    if 'levo' in td['class']:
        grad = td.string
        found = True

for x in prognoza:
    print(x)   

# for child in soup.find_all('tr') if child.
#     print(child)