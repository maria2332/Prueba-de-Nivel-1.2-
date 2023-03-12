"""
Ahora quedará a cargo del alumno completar la funcionalidad del TDA polinomio, dado que solo se desarrollaron algunas funciones, 
agregándole la capacidad de eliminar términos, y de determinar si en un polinomio existe un término, para evitar tener que llamar a la función “obtener_valor” 
y luego consultar si el resultado es distinto de cero para determinar si el polinomio tiene ese término o no. Esta última debe ser una función booleana.
"""

class Nodo(object): 
    """Clase nodo simmplemente enlazado"""

    info, sig = None, None

class datoPolinomio(object):
    """Clase dato polinomio"""

    def __init__(self, valor, termino):
        """Crea un dato polinomio con valor y término"""
        self.valor = valor # coeficiente
        self.termino = termino # exponente


class Polinomio(object):
    """Clase polinomio"""

    def __init__(self):
        """Crea un polinomio del grado cero"""
        self.termino_mayor = None
        self.grado = -1

    def agregar_termino(polinomio, termino, valor):
        """Agrega un termino y su valor al polinomio"""
        aux = Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if (termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else:
            actual = polinomio.termino_mayor
            while (actual.sig is not None and termino < actual.sig.info.termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux

    def modificar_termino(polinomio, termino, valor):
        """Modifica un termino del polinomio"""
        aux = polinomio.termino_mayor
        while (aux is not None and aux.info.termino != termino):
            aux = aux.sig
        aux.info.valor = valor

    def obtener_valor(polinomio, termino):
        """Devuelve el valor de un termino del polinomio"""
        aux = polinomio.termino_mayor
        while (aux is not None and aux.info.termino != termino):
            aux = aux.sig
        if (aux is not None and aux.info.termino == termino):
            return aux.info.valor
        else:
            return 0
        
    def eliminar_termino(polinomio, termino):
        """Elimina un termino del polinomio"""
        aux = polinomio.termino_mayor
        if (aux is not None and aux.info.termino == termino):
            polinomio.termino_mayor = aux.sig
        else:
            while (aux.sig is not None and aux.sig.info.termino != termino):
                aux = aux.sig
            if (aux.sig is not None and aux.sig.info.termino == termino):
                aux.sig = aux.sig.sig

    def existe_termino(polinomio, termino):
        """Determina si existe un termino en el polinomio"""
        aux = polinomio.termino_mayor
        while (aux is not None and aux.info.termino != termino):
            aux = aux.sig
        if (aux is not None and aux.info.termino == termino):
            return True
        else:
            return False
        
    def mostrar(polinomio):
        """Muestra el polinomio"""
        aux = polinomio.termino_mayor
        pol = ""
        if (aux is not None):
            while (aux is not None):
                signo = ""
                if aux.info.valor >= 0:
                    signo += "+"
                pol += signo + str(aux.info.valor) + "x^" + str(aux.info.termino)
                aux = aux.sig
        return pol
    
    def sumar(polinomio1, polinomio2):
        """Suma dos polinomios y devuelve el resultado"""
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0, mayor.grado + 1):
            total = Polinomio.obtener_valor(polinomio1, i) + Polinomio.obtener_valor(polinomio2, i)
            if (total != 0):
                Polinomio.agregar_termino(paux, i, total)
        return paux
        
    def restar(polinomio1, polinomio2):
        """Resta dos polinomios y devuelve el resultado"""
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0, mayor.grado + 1):
            total = Polinomio.obtener_valor(polinomio1, i) - Polinomio.obtener_valor(polinomio2, i)
            if (total != 0):
                Polinomio.agregar_termino(paux, i, total)
        return paux

    def multiplicar(polinomio1, polinomio2):
        """Multiplica dos polinomios y devuelve el resultado"""
        paux = Polinomio()
        pol1 = polinomio1.termino_mayor
        while (pol1 is not None):
            pol2 = polinomio2.termino_mayor
            while (pol2 is not None):
                termino = pol1.info.termino + pol2.info.termino
                valor = pol1.info.valor * pol2.info.valor
                if (Polinomio.obtener_valor(paux, termino) != 0):
                   valor += Polinomio.obtener_valor(paux, termino)
                   Polinomio.modificar_termino(paux, termino, valor)
                else:
                    Polinomio.agregar_termino(paux, termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux


p1 = Polinomio()
p1.agregar_termino(3, 7) # Agrega el término 7x^3
p1.agregar_termino(5, -2) # Agrega el término -2x^5

p2 = Polinomio()
p2.agregar_termino(4, 7) # Agrega el término 7x^4
p2.agregar_termino(1, 1) # Agrega el término x (X^1)

print(p1.mostrar()) # Muestra el polinomio 1
print(p2.mostrar()) # Muestra el polinomio 2
print(p1.obtener_valor(7)) # Devuelve el coeficiente del término x^7
print(p2.obtener_valor(1)) # Devuelve el coeficiente del término x^1

p3 = Polinomio.sumar(p1, p2) # Suma los polinomios p1 y p2
print(p3.mostrar()) 

p4 = Polinomio.multiplicar(p1, p2) # Multiplica los polinomios p1 y p2
print(p4.mostrar()) 

p5 = Polinomio.restar(p2, p1) # Resta los polinomios p1 y p2
print(p5.mostrar()) 

p1.eliminar_termino(3) # Elimina el término 7x^3 del polinomio p1
print(p1.mostrar()) 

print(p1.existe_termino(5)) # Devuelve True si existe el término x^5 en el polinomio p2
print(p2.existe_termino(3)) # Devuelve False si no existe el término x^3 en el polinomio p2


