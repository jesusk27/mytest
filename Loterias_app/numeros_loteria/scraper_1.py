from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

def  get_soup():
    url ='https://leidsa.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #loterias = {}
    
def get_loto(soup):
    # conseguir los numeros del loto
    nos_loto = soup.select('.numeros-ganadores-pc span')
    nos_loto = [n.text.replace('\n', '').replace('\t', '') for n in nos_loto]
    loterias['loto'] = nos_loto
    fecha_res= soup.find_all('p')[1].get_text()
    #fecha_res = nos_loto.parent.select_one('.resultados-del-dia').text
    # serie = pd.Series(nos_loto, name='loto')
    # return serie
    return {
     
      'nos_loto'  : nos_loto,
      'fecha_res' : fecha_res
    }

def get_other(soup):
    # conseguir las demas loterias

    panels = soup.find_all('div', class_='panel-default')
    lotos=[]
    for panel in panels:
        loto_name = panel.find('img').attrs['src'].split('logo')[1][1:-4]
        numeros = panel.select('.numeros-sorteos td')
        numeros = [n.text.replace('\n', '').replace('\t', '') for n in numeros]
        numeros = [n for n in numeros if n != '']
        loterias[loto_name] = numeros
        #fecha_res = soup.find_all('p' ,class_= 'fecha-sorteos')
        #fecha_res = [d.get_text() for d in fecha_res]
        fecha_res = panel.parent.select_one('.fecha-sorteos').text
        lotos.append({
            
           'loto_name'  : loto_name,
            'numeros'   : numeros,
            'fecha_res' : fecha_res
        })

        return lotos
            
def get_loterias():   

  #loterias = {}
  #get_loto(soup)
  #get_other(soup)

  soup = get_soup()
  loto1 = get_loto(soup)
  others = get_other(soup)
  others.append(loto1)

  #print(loterias)

  #return loterias
  return others


#df = pd.concat([serie_lotos, serie_otros], axis=1)
#df = df.replace('s', '-', regex=True)
#df = df.replace(np.nan, '-', regex=True)
#print(df)
