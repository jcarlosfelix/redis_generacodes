# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:57:41 2020

@author: jcarl
"""

import redis
import os
import time
import random

from alimentar_metodos import get_alfanum


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


#Agregamos cadenas alfanumericas de entre 4 a 6 caracteres.
while True:
    cadena, x = '', 0
    longitud = random.randint(4, 6)

    while x < longitud:
        cadena += get_alfanum()
        x += 1

    r.rpush('lista_segmentos', cadena)    
    #print(' .. ' + cadena)
    time.sleep(random.randint(1, 3)/3)