

#def indeterminado_x_nombre(**kwargs):
#    print(type(kwargs))

#    for clave, valor in kwargs.items:
#        print(clave, valor)
#        indeterminado_x_nombre(nombre_1= "Matias", nombre_2= "Ivan")


# //////////////////////////////////////
# def funcion(*args, **kwargs):
#     total = 0

#     for arg in args:
#         total += arg

#     print(f'La sumatoria es: {total}')


#     for kwarg in kwargs:
#         print(kwarg)

# funcion(10 , 5, -7, 3, 45, nombre='Matias', edad=28)

# /////////////////////////////////

# n=int(input('Que table de multiplicar quiere ver? Ingrese número: '))

# def tabla_de_multiplicar(n):

#     for i in range(1,11):
#         print(n, '*', i, '=', n*i)

# tabla_de_multiplicar(n)

# def saludo():

#     return 'Hola mundo!! '
# print(saludo())
#//////--------/////////---------//////-------///-//////-///-////
# 17)_ Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una
# cadena con un espacio adicional tras cada letra.
#  Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use
# dicha función.


texto = str(input('Ingrese texto: '))

def convertir_espacios(texto):
    for i in texto:
        print(i)
        
        if i != ' ':
            i = ' '
            print(i)

convertir_espacios(texto)