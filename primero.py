class NodoCircular:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class ListaCircular:
    def __init__(self):
        self.head = None
        self.prev= None
        self.end= None

    def insertar_final(self, dato):
        nuevo = NodoCircular(dato)
        conteo=0

        if not self.head:
            self.head = nuevo
            nuevo.next = self.head
            return

        actual = self.head
        while actual.next != self.head:
            actual = actual.next

        actual.next = nuevo
        self.end=nuevo
        nuevo.next = self.head
        conteo=conteo+1
        self.prev=self.end

    def crear_lista(self, n):
        for i in range(1, n + 1):
            self.insertar_final(i)

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        resultado = []
        actual = self.head

        while True:
            resultado.append(str(actual.dato))
            actual = actual.next
            if actual == self.head:
                break

        print(" -> ".join(resultado) + " -> (ciclo)")

    def josephus_modificado(self, m,n):
        current= self.head
        self.conteo= 1
        i=0
        while m<n:
            while i<m-1:
                i=i+1
                self.prev=self.prev.next
                current=current.next
            current.next=None
            current.next=current.next.next
            conteo=conteo+1
            if current.next%5 ==0:
                self.head=current.prev
            else:
                self.head=current



