class Pila:
    lista = []

    def push(self,elemento):
        self.lista.append(elemento)

    def pop(self):
        return self.lista.pop()

    def empty(self):
        if self.lista:
            return False
        return True

class Cola:
    cola = []

    def encolar(self, elemento):
        self.cola.append(elemento)

    def desencolar(self):
  	desencolado = self.cola[0]
        self.cola = self.cola[1:]
        return desencolado

    def empty(self):
        if self.cola:
            return False
        return True
