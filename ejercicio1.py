"""
Ahora quedará a cargo del alumno completar la funcionalidad del TDA polinomio, dado que solo se desarrollaron algunas funciones, 
agregándole la capacidad de eliminar términos, y de determinar si en un polinomio existe un término, para evitar tener que llamar a la función “obtener_valor” 
y luego consultar si el resultado es distinto de cero para determinar si el polinomio tiene ese término o no. Esta última debe ser una función booleana.
"""

class Nodo(object):
    """clase nodo simplemente enlazado."""
    info, sig = None, None

# aux = Nodo( )
# aux.info = "Primer nodo"
# palabra = input('Ingrese una palabra: ')	
# naux = aux
# while (palabra != ""):
#     nodo = Nodo( )
#     nodo.info = palabra
#     naux.sig = nodo
#     naux = nodo
#     palabra - input('Ingrese una palabra: ')
# while (aux is not None):
#     print(aux.info)
#     aux = aux.sig

class datoPolinomio(object):    
    """Clase dato polinomio."""

    def __init__(self, valor, termino):
        """Crea un dato polinomio con valor y termino."""
        self.valor = valor
        self.termino = termino

class Polinomio(object):
    """Clase polinomio."""

    def __init__(self):
        """Crea un polinomio del grado cero."""
        self.termino_mayor = None
        self.grado = -1

def agregar_termino(polinomio, termino, valor):
    """Agrega un termino y su valor al polinomio. """
    aux = Nodo( )
    dato = datoPolinomio(valor, termino)
    aux.info = dato
    if(termino > polinomio.grado):
        aux.sig = polinomio.termino_mayor
        polinomio.termino_mayor = aux
        polinomio.grado = termino
    else:
        actual = polinomio.termino_mayor
        while(actual.sig is not None and termino < actual.sig.info.termino):
            actual = actual.sig
        aux.sig = actual.sig
        actual.sig = aux

def modificar_termino (polinomio, termino, valor):
    "" "Modifica un termino del polinomio."""
    aux = polinomio.termino_mayor
    while(aux is not None and aux.info.termino != termino):
        aux = aux.sig
    aux.info.valor = valor

def obtener_valor (polinomio, termino):
    """Devuelve el valor de un termino del polinomio."""
    aux = polinomio.termino_mayor
    while(aux is not None and aux. info.termino > termino):
        aux = aux.sig
    if(aux is not None and aux.info.termino == termino): 
        return aux.info.valor 
    else:
        return 0

def mostrar (polinomio):
    """Muestra el polinomio."""
    aux = polinomio.termino_mayor
    pol = ''
    if (aux is not None):
        while(aux is not None):
            signo = '' 
            if(aux. info.valor > 0):
                signo += '+'
            pol += signo + str(aux.info.valor)+"x^"+str(aux.info.termino)
            aux = aux.sig
    return pol

def sumar(polinomio1, polinomio2):
    """Suma dos polinomios y devuelve el resultado."""
    paux = Polinomio()
    mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2 
    for i in range(0, mayor.grado+1):
        total = obtener_valor(polinomio1, 1) + obtener_valor (polinomio2, i)
        if(total != 0):
            agregar_termino(paux, i, total)
    return paux

def multiplicar(polinomio1, polinomio2):
    """Multiplica dos polinomios y devuelve el resultado."""
    paux = Polinomio()
    pol1 = polinomio1.termino_mayor
    while(pol1 is not None):
        pol2 = polinomio2.termino_mayor
        while(pol2 is not None):
            termino = pol1.info.termino + pol2.info. termino
            valor = pol1.info.valor * pol2.info. valor
            if(obtener_valor (paux, termino) != 0):
                valor += obtener_valor (paux, termino)
                modificar_termino(paux, termino, valor)
            else:
                agregar_termino (paux, termino, valor)
            pol2 = pol2.sig
        pol1 = pol1.sig
    return paux

def eliminar_termino(polinomio, termino):
    """Elimina un termino del polinomio."""
    aux = polinomio.termino_mayor
    if(aux is not None):
        if(aux.info.termino == termino):
            polinomio.termino_mayor = aux.sig
            if(polinomio.grado == termino):
                polinomio.grado = -1
        else:
            while(aux.sig is not None and aux.sig.info.termino != termino):
                aux = aux.sig
            if(aux.sig is not None):
                aux.sig = aux.sig.sig
                if(polinomio.grado == termino):
                    polinomio.grado = aux.info.termino

def existe_termino(polinomio, termino):
    """Devuelve True si el termino existe en el polinomio."""
    aux = polinomio.termino_mayor
    while(aux is not None and aux.info.termino > termino):
        aux = aux.sig
    if(aux is not None and aux.info.termino == termino):
        return True
    else:
        return False
    
    
def main():
    """Funcion principal."""
    polinomio1 = Polinomio()
    polinomio2 = Polinomio()
    agregar_termino(polinomio1, 0, 1)
    agregar_termino(polinomio1, 1, 2)
    agregar_termino(polinomio1, 2, 3)
    agregar_termino(polinomio1, 3, 4)
    agregar_termino(polinomio2, 0, 5)
    agregar_termino(polinomio2, 1, 6)
    agregar_termino(polinomio2, 2, 7)
    agregar_termino(polinomio2, 3, 8)
    print("Polinomio 1: ", mostrar(polinomio1))
    print("Polinomio 2: ", mostrar(polinomio2))
    print("Suma: ", mostrar(sumar(polinomio1, polinomio2)))
    print("Multiplicacion: ", mostrar(multiplicar(polinomio1, polinomio2)))
    print("Existe el termino 2 en el polinomio 1: ", existe_termino(polinomio1, 2))
    print("Existe el termino 4 en el polinomio 1: ", existe_termino(polinomio1, 4))
    eliminar_termino(polinomio1, 2)
    print("Polinomio 1: ", mostrar(polinomio1))
    modificar_termino(polinomio1, 1, 10)
    print("Polinomio 1: ", mostrar(polinomio1))
    print("Valor del termino 1 en el polinomio 1: ", obtener_valor(polinomio1, 1))
    print("Valor del termino 2 en el polinomio 1: ", obtener_valor(polinomio1, 2))




