from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

url ='https://leidsa.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
loterias = {}

def get_loto(soup):
    # conseguir los numeros del loto
    nos_loto = soup.select('.numeros-ganadores-pc span')
    nos_loto = [n.text.replace('\n', '').replace('\t', '') for n in nos_loto]
    loterias['loto'] = nos_loto
    # serie = pd.Series(nos_loto, name='loto')
    # return serie

def get_other(soup):
    # conseguir las demas loterias

    panels = soup.find_all('div', class_='panel-default')
    for panel in panels:
        loto_name = panel.find('img').attrs['src'].split('logo')[1][1:-4]
        numeros = panel.select('.numeros-sorteos td')
        numeros = [n.text.replace('\n', '').replace('\t', '') for n in numeros]
        numeros = [n for n in numeros if n != '']
        loterias[loto_name] = numeros

def get_loterias():   
  #loterias = {}
  get_loto(soup)
  get_other(soup)

  #print(loterias)

  return loterias


#df = pd.concat([serie_lotos, serie_otros], axis=1)
#df = df.replace('s', '-', regex=True)
#df = df.replace(np.nan, '-', regex=True)
#print(df)
