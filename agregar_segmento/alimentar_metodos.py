import random


def get_alfanum():
	return {True: get_carater(), False: get_numero()} [random.randint(0, 1) == 1]

def get_numero():
	return str(random.randint(0, 9))

def get_carater():
	return calcular_caracter(random.randint(1, 26))


#Retorna un caracter a partir de un indice
def calcular_caracter(indice):
    diccionario = { 
        1: 'A', 
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'F',
        7: 'G',
        8: 'H',
        9: 'I',
        10: 'J',
        11: 'K',
        12: 'L',
        13: 'M',
        14: 'N',
        15: 'O',
        16: 'P',
        17: 'Q',
        18: 'R',
        19: 'S',
        20: 'T',
        21: 'U',
        22: 'V',
        23: 'W',
        24: 'X',
        25: 'Y',
		26: 'Z',
        #Default: VACIO
    } 
  
    return diccionario.get(indice, '')
