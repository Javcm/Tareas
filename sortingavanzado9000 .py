
# coding: utf-8

# In[57]:


#Código para ordenar una lista de datos 
#Autor: Javier Carrillo Martínez



def sort(x):            #Función de ordenamiento sort, variable una lista de número
    i=0
    l=len(x)
    for j in range(l-1,0,-1):       #Primer for para ordenar los elementos de la lista l-1 veces
        for i in range(j):          #Segundo for para ordenar uno a uno los elementos 
            if x[i]>x[i+1]:
                z=x[i]             
                x[i]=x[i+1]
                x[i+1]=z
            i=i+1                  #contador
    return(x)                      #el output es la lista de datos ya ordenada

debug = True #Cambien este valor a False para pedir los datos al usuario

#Arreglo de entrenamiento
text = "6,3,9,5,1,7,1"

if not debug:
    text = input("Ingrese una secuencia de valores naturales separados por coma: ")

#Convertimos la cadena de caracteres en una lista
values = [int(i) for i in text.split(',')]

x=sort(values)

print(x)

