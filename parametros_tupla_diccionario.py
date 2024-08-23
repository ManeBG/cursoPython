# Parametros de tipo tupña, *args

def promedio (*numeros):
    """
    Recibe un solo parametro de tipo tupla, de valores numericos 
    E imprime su promedio
    """
    promedio = sum(numeros)/len(numeros)
    print('El promedio es:', promedio)

promedio(4)
promedio(4, 5, 6)
promedio(1, 2, 3, 4, 5, 6, 7, 8, 9)

def es_numero(titulo, *serie):
    """
    Imprime un titulo
    Verifica si el caracter en el parametro de tipo tupla es un numero o no
    """
    print(titulo)
    for i in serie:
        if type(i)  == int or i.isdigit():
            print(f'{i} es un numero')
        else:
            print(f'{i} no es numero')

es_numero('Numeros', '1', '2', '3')
es_numero('Letras', 'a', 'b', 'c')

nombre = 'Mezcla'
lista_varios = ['a', '2', '3', 'f', '5']
es_numero(nombre, *lista_varios)

#######################################################

# Parametros tipo diccionario **kwargs

def area(**dato): # **dato es una variable que reccibe un diccionario
    """ Calcula el area de una figura geometrica y la imprime en ppantalla.""" # Docstring

    # Si el diccionario tiene una clave llamada 'figura' evalua el valor de la clave
    if dato["figura"]=="Rectangulo":
        print(dato["base"]*dato["altura"]) # Si el valor de la clave es 'Rectangulo' impriime el valor de la clave 'base' multiplicada por 'altura'
    elif 