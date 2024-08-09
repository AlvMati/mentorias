#n=int(input('ingrese un número: '))
#diccionario={}
#/////////////////////////////////////// pruebas
#diccionario={
#'pais' : 'Argentina',
#'provincia': 'Chaco',
#'cuidad': 'Resistencia',
#'cp': 3500}

#print(diccionario)
#print(diccionario['pais'])

#diccionario['departamento'] = 'Sanfernando'
#print(diccionario)

#diccionario['pais'] = 'alemania'
#print(diccionario)
#///////////////////////////////////// fin pruebas

#---------------------------///////////////
texto=str(input('Ingrese un texto por favor: '))
dic={}
texto_2=texto.lower()

for i in texto:
    if i != '':
        if i in dic:
            dic[i] +=1
        else:
            dic[i] = 1
    else:
        i= i+1    
print(dic)

