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
    dias_venta=dias_venta.replace("De venta todos los díasSorteos Miércoles y Sábado", "Sorteos Miércoles y Sábado")
    fecha_res = nos_loto.parent.select_one('.resultados-del-dia').text
    nos_loto = nos_loto.select('span')
    nos_loto = [n.text.replace('\n', '').replace('\t', '') for n in nos_loto]
    loto_acum=""
    #loto_acu=list()
    #acu = soup.select('div.panel-heading.panel-heading-millones-acumulados > p')
    #acu2 = soup.select('div.wraper-millones-acumulados > p')
    #for a in acu:
       #loto_acu.append(a.text)
    #for ac in acu2:
        #loto_acu.append(ac.text)

    #loto_ac = soup.select_one('div.panel-heading.panel-heading-millones-acumulados > p').text.strip() 
    #for acu in loto_ac:
         #loto_acu.append(acu.text) 
    #loto_ac2=
    #for acu in loto_acu:
     #loto_acu.append(acu.text)  
    
    return {
      'loto_name' : 'loto',
      'numeros' : nos_loto,
      'dias_venta' : dias_venta,
      'fecha_res' : fecha_res,
      'loto_acum' : loto_acum
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
        dias_venta = dias_venta.replace("De venta todos los días"," ")
        #dias_venta = dias_venta.replace("Sorteo de Lunes a Sábado a las 08:55 PM / Domingos 05:55 PM","Sorteo de Lun a Sáb a las 08:55 PM|Dom 05:55 PM")
        fecha_res = panel.parent.select_one('.fecha-sorteos').text
        loto_acum = ""
        #panel.parent.select_one('.div.panel-heading.panel-heading-millones-acumulados > p')  
        lotos.append({
            'loto_name' : loto_name,
            'numeros' : numeros,
            'dias_venta' : dias_venta,
            'fecha_res' : fecha_res,
            'loto_acum': loto_acum
        
        })

    return lotos

    
def get_acumulado(soup):
    acu = soup.find_all('p' ,class_='txt2-acumulado text-center')
    #acu2 = soup.find_all('p' ,class_='txt4-acumulado text-center')
    #acu2 = soup.find_all('p' ,class_='txt6-acumulado text-center')
    #acu = soup.select('div.panel-heading.panel-heading-millones-acumulados > p')
    #acu2 = soup.select('div.wraper-millones-acumulados > p')
    #acu2 = acu2.replace("15 MILLONESLOTO 61 MILLONESLOTO MAS 200","15 + 61 + 200")
    acumulado=''
    acumulado+=''.join(map(lambda a:a.text + ' ',acu))
    #acumulado+=''.join(map(lambda a:a.text + ' ',acu2))
    
    return acumulado


def get_acumuladoloto(soup):
    acu2 = soup.find('p' ,class_='txt4-acumulado text-center')
    acumuladoloto=''
    acumuladoloto+=''.join(map(lambda b:b + ' ',acu2))
    
    return acumuladoloto

def get_acumuladomas(soup):
    acu3 = soup.find_all('p' ,class_='txt6-acumulado text-center')
    acumuladomas=''
    acumuladomas+=''.join(map(lambda a:a.text + ' ',acu3))
    #acumulado+=''.join(map(lambda a:a.text + ' ',acu2))
    
    return acumuladomas



def get_ganador(soup):
    n_win = soup.find_all("p", class_="nombre-ganador")
    win=soup.find_all("span" ,class_="txt-info-ganador-1")
    ganador=''
    ganador+=''.join(map(lambda g:g.text + ' ',n_win))
    ganador+=''.join(map(lambda g:g.text + ' ',win))

    return ganador

def get_iganador(soup):
    iganador = []
    i_win = soup.findAll("img" ,class_="img-ganador img-responsive")
    for image in i_win:
        iganador=(image['src']) 
         
    
    return iganador


def get_loterias():
  soup = get_soup()
  loto1 = get_loto(soup)
  others = get_other(soup)
  loto_acum = get_acumulado(soup)
  loto_acum2= get_acumuladoloto(soup)
  loto_mas = get_acumuladomas(soup)
  loto_win = get_ganador(soup)
  loto_iwin= get_iganador(soup)
  others.append(loto1)

  return {
     'loterias':others,
     'acumulado':loto_acum,
     'ganador':loto_win,
     'iganador':loto_iwin,
     'acumuladoloto':loto_acum2,
     'acumuladomas':loto_mas
   
  }
  
 
