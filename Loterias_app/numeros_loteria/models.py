from django.db import models
from numeros_loteria.scraper import get_loterias
# Create your models here.
class NumeroLoteria():

    def __init__(self):
        self.nombre = None
        self.numeros = None
        self.dias_venta = None
        self.fecha_res = None  
        #self.loto_acum=None      


    @staticmethod
    def devolver_numeros():
        numeros = get_loterias()   
        loterias = [] 
        for numero in numeros['loterias']:
            loteria = NumeroLoteria()
            loteria.nombre = numero['loto_name']
            loteria.numeros = numero['numeros']
            loteria.dias_venta = numero['dias_venta']
            loteria.fecha_res = numero['fecha_res']
            loterias.append(loteria)
            
        datosLoteria = DatosLoteria()
        datosLoteria.loterias = loterias
        datosLoteria.acumulado = numeros['acumulado']
        datosLoteria.acumuladoloto = numeros['acumuladoloto']
        datosLoteria.acumuladomas = numeros['acumuladomas']
        datosLoteria.ganador = numeros['ganador']
        datosLoteria.iganador = numeros['iganador']
        
        return datosLoteria

class DatosLoteria():
    pass

class DatosGanador():
    pass

class datoslotos():

    def __init__(self):
        self.loto_acum = None
        
    #@staticmethod
    #def devolver_acumulado():
        #acum = get_acumulados() 
        #acu = datoslotos()
        #for d in acum:
        #acu.loto_acum=['loto_acum']

            #loteria.loto_acum=numero['loto_acum']
        #al=acum['loto_acum']
        #print(al)
        #acu.loto_acum=acum['loto_acum']
        #loto_ac=[]
        #loto_ac.append(acu)
        #import ipdb; ipdb.set_trace(context=22)
        #return loto_ac


