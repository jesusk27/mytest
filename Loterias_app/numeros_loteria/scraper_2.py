from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


def get_soup():
  url ='https://leidsa.com/'
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  return soup


def get_loto(soup):
    # conseguir los numeros del loto
    nos_loto = soup.select_one('.numeros-ganadores-pc')
    dias_venta = nos_loto.parent.select_one('.txt-dias-ventas').text
    fecha_res = nos_loto.parent.select_one('.resultados-del-dia').text
    
    nos_loto = nos_loto.select('span')

    nos_loto = [n.text.replace('\n', '').replace('\t', '') for n in nos_loto]

    return {
      'loto_name' : 'loto',
      'nos_loto' : nos_loto,
      'dias_venta' : dias_venta,
      'fecha_res' : fecha_res
    }


def get_other(soup):
    # conseguir las demas loterias

    panels = soup.find_all('div', class_='panel-default')
    lotos = []
    for panel in panels:
        loto_name = panel.find('img').attrs['src'].split('logo')[1][1:-4]
        numeros = panel.select('.numeros-sorteos td')
        numeros = [n.text.replace('\n', '').replace('\t', '') for n in numeros]
        numeros = [n for n in numeros if n != '']
        dias_venta = panel.parent.select_one('.txt-ventas-dias').text
        fecha_res = panel.parent.select_one('.fecha-sorteos').text
        lotos.append({
            'loto_name' : loto_name,
            'numeros' : numeros,
            'dias_venta' : dias_venta,
            'fecha_res' : fecha_res
        })

        return lotos
    

def get_loterias():
  soup = get_soup()
  loto1 = get_loto(soup)
  others = get_other(soup)
  others.append(loto1)

  return others

