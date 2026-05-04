class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class ListaSimple:
    def __init__(self):
        self.head = None
        self.prev= None
        self.end=None
        self.sig=None
        

    def insertar_final(self, dato):
        nuevo = NodoSimple(dato)

        if not self.head:
            self.head = nuevo
            return
        
        actual = self.head
        self.prev=self.head
        while actual.next:
            self.prev=self.prev.next
            actual = actual.next

        actual.next = nuevo
        
        self.end=nuevo

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        actual = self.head
        resultado = []

        while actual:
            resultado.append(str(actual.dato))
            actual = actual.next

        print(" -> ".join(resultado) + " -> None")

    def partir(self):
        l=self.head
        r=self.end
        while l!=r:
            l=l.next
            if r.prev==l:
                r=r.prev
        return r,l
    def rever(self):
        partir()
        current=r
        while r.next!=None or current.next!=None:

    def intercalar(self):
