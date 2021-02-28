# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:57:41 2020

@author: jcarl
"""

import redis
import os
import time


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
print('setup:espera 4 segundos')
time.sleep(4)


while True:
    codigo = r.lpop('lista_codigos')

    if codigo is None:
        print('se agotaron los elementos')
        break

    print('Codigo: ' + codigo)
    time.sleep(0.5)