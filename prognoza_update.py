#!/usr/bin/env python

from pathlib import Path            #file manipulation  
from unicodedata import normalize   #for cyrilic

import urllib.request as url        #grabbing HTML
from bs4 import BeautifulSoup       #getting data out of HTML (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)


PISMO_LATINICA = True          #latin or cyrilic


#get web page 
if PISMO_LATINICA :
    page = url.urlopen('http://www.hidmet.gov.rs/latin/osmotreni/index.php')
else:
    page = url.urlopen('http://www.hidmet.gov.rs/ciril/osmotreni/index.php')


#get weather data and 
soup = BeautifulSoup(page, features='html.parser')
text = ""
found = False
for td in soup.findAll('td', {'class':['bela75', 'siva75']}):
    if found:
        text += " {}°C    ".format(td.string.strip())
        found = False
        continue
    if 'levo' in td['class']:
        text += "".join(normalize('NFKD', td.string).upper().split()) 
        found = True

#update .txt file with data from weather[]

dir = Path()
file_path = dir / 'TEMPERATURA PO GRADOVIMA.txt'
with file_path.open('w', encoding ='utf-8') as f:
    f.write(text)




# for child in soup.find_all('tr') if child.
#     print(child)