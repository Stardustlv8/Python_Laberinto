#algoritmo de busqueda primero a lo ancho

#Toma la posicion actual del laberinto
#retorna el siguiente estado valido
from Estados import adyacentes, en_visitados
from Split import crea_laberinto, impLab
from Estructuras import Cola
from run_laberinto import run_lab

def search_BFS(inicial, laberinto):
    lab = crea_laberinto(laberinto)
    cola = Cola()
    visitados = []
    Estructura = []
    visitados.append(inicial)
    cola.encolar(inicial)
    print "Estado inicial: ",inicial
    while not cola.empty():
        v = cola.desencolar()
#---------------------------------------------
	run_lab(v,lab)
       	print "Estado Desencolado: ", v
       	print "Cola: ", cola.cola
       	r = raw_input(" ")
#---------------------------------------------
        for w in adyacentes(v,lab):
            if not en_visitados(w,visitados):
                visitados.append(w)
                cola.encolar(w)
#---------------------------------------------
                run_lab(v,lab)
                print "Estado actual: ", v
                print "Estados validos: ", adyacentes(v,lab)
                print "Estado sucesor: ", w
                print "Estado Encolado: ", w
                print "Pila: ", cola.cola
                r = raw_input(" ")
#---------------------------------------------

    return visitados


