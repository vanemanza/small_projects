import random

"""
hacer q aparezcan todas las letras cuando hay mas de una,
que cuando acertas una letra te suma una chance,
Ofrecer la opcion de agregar una letra o arriesgar la palabra
Cuando se adivina la palabra tiene que cortar
Si ingresa un numero o elem no valido dar error"""

def elegir_palabra():

    palabras = ['filet', 'aceite', 'auricular', 'frasco', 'murcielago', 'pokemon', 'cortina', 'hectoplasma', 'lagarta', 'libro', 'musica', 'trincheta', 'comida']

    palabra = random.choice(palabras)

    return palabra

def arriesgar_letra():
    
    letra = input('Ingresa una letra:   ')    
                
    return letra 

def reemplazar_letras():
    palabra = elegir_palabra()
    incognita = '-'*len(palabra)    
    letras = []    
    chances = len(palabra)
        
    while len(letras) < len(palabra):
        letra = arriesgar_letra() #hace falta hacer una funcion separada ? o pongo el input aquí?
                
        if letra in palabra:
            posicion = palabra.index(letra)
            chances +=1
            
            for x, y in enumerate(incognita):
                if x == posicion:
                    l = list(incognita)
                    l[x] = letra
                    incognita = "".join(l)
                    print(incognita)
                                    
        else:
            chances -=1
            print(f'La letra {letra} no se encuentra en esta palabra.') 
            print(f'Te quedan {chances} chances, inténtalo de nuevo.') 
            
        letras.append(letra)    
        
    return palabra, letras

test =reemplazar_letras()
print(test)
