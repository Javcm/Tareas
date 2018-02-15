#Programa para ver cuántos turbopalíndromos hay del 1 al 200000
#Autor: Javier Carrillo Martínez

# coding: utf-8

# In[11]:


import numpy as np   #importamos la librería numpy que nos permitirá trabajar con verctores 


# In[12]:


def number_to_string(x):     #construimos esta función para acomodar los dígitos de x en una lista de strings, convirtiéndolo primero en strings y luego concatenándolos 
    string = str(x)          
    digits = []
    for letter in string:
        digits = np.append(digits, letter)
    return list(digits)


# In[13]:


def palindromo(x):   #Esta función nos permite saber si un número(x) es palíndromo (dato curioso, palíndromo es para palabras, capicúo es para números)
    string = number_to_string(x)
    a = list(reversed(string))
    if a == string: return 1
    else: return 0      #si es palíndromo devuelve 1, si no devuelve 0


# In[39]:


def rot(x, a):       #Esta es la función rotación de x en a 
    s = ''           #se define "s" como "nada", para juntar más tarde los dígitos de la rotación 
    string = number_to_string(x)  
    l = len(string)    
    a = a % l   #Dado que a lo más x es de 6 dígitos, hay 6 rotaciones, sólo es necesario definir estas 
    a = l-a    
    aux = np.concatenate([string[a:],string[:a]])  #se concatenan los últimos a dígitos con los primeros a 
    aux = list(aux)
    aux = s.join(aux)    #juntamos los elementos ya rotados
    return int(aux)


# In[33]:


def turbo(x):      #está es la función para evaluar si un número es turbopalíndromo o no
    string = number_to_string(x)
    r = 0
    i = 0
    for digit in string:
        a = int(digit)
        r = r + (-1)**i*rot(x, a)
        i+=1
    r = r + x
    r = abs(r)
    if palindromo(r) == 1: return 1    #si lo es devuelve 1, si no devuelve 0
    else: return 0


# In[60]:


top = 200000          #cota superior para contar los turbopalíndromos
numbers = np.linspace(1, top, top, dtype = int)


# In[61]:


tpalindromos = np.array([], dtype = int)    #crea una lista con todos los números turbopalíndromos del 1 al top
for n in numbers:
    if turbo(n)==1: 
        tpalindromos = np.append(tpalindromos, n)


# In[62]:


len(tpalindromos)    #devuelve el número de turbopalíndromos del 1 al top, para 200000 el número de turbopalíndromos que me arrojó fue de 1224 

