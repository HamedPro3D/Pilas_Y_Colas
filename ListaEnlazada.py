from Nodo import *

class ListaEnlazada():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None
    
    def pila(self,dato):
        if self.vacia() == True:
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)

    def cola(self,dato):
        if self.vacia() == True: 
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero =  aux

    def recorrido(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente

    def salidaPila(self):
        aux = self.primero
        while aux.siguiente != self.ultimo:
            aux = aux.siguiente
        print("se leyo: ",self.ultimo.dato," el siguiente libro a leer sera: ",aux.dato)
        aux.siguiente = None
        self.ultimo = aux

    def salidaCola(self):
        aux = self.primero
        self.primero = self.primero.siguiente
        print("Salio: ",aux.dato, " de la fila")