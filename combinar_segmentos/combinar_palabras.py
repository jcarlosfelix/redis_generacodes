# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:57:41 2020

@author: jcarl
"""

import redis
import os
import time
import random


#Restringe redis a codificar-decodificar los mensajes como string con "charset='utf-8', decode_responses=True"
r = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=6379, db=0, charset='utf-8', decode_responses=True)
redis_ready = False

while not redis_ready:
    try:
        redis_ready = r.ping()
    except:
        print('waiting for redis')
        time.sleep(3)
        
print('setup:redis alive')
print('setup:espera 2 segundos')
time.sleep(2)


#Inicializamos los valores. Una combinación se compone por 2 a 5 cadenas.
combinacion, x = '', 0
num_elementos = random.randint(2, 5)


while True:    
    cadena = r.lpop('lista_segmentos')

    if cadena is None:
        print('se agotaron los elementos')
        break

    combinacion += {True: cadena, False: '-' + cadena} [combinacion == '']
    x += 1

    if (x == num_elementos):
        r.rpush('lista_codigos', combinacion)

        #Reiniciamos los valores de combinacion
        combinacion, x = '', 0
        num_elementos = random.randint(2, 5)        
        time.sleep(0.5)