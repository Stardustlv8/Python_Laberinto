from Estados import adyacentes, en_visitados
from Split import crea_laberinto, impLab
from Estructuras import Pila
from run_laberinto import run_lab

def search_DFS(inicial, laberinto):
    lab = crea_laberinto(laberinto)
    pila = Pila()
    visitados = []
    visitados.append(inicial)
    pila.push(inicial)
    print "Estado inicial: ", inicial
    while not pila.empty():
        v = pila.pop()
#--------------------------------------------------------
	run_lab(v,lab)
	print "Estado Desempilado: ", v
	print "Pila: ", pila.lista
	r = raw_input(" ")
#--------------------------------------------------------
        for w in adyacentes(v,lab):
            if not en_visitados(w,visitados):
                visitados.append(w)
                pila.push(w)
#--------------------------------------------------------
		run_lab(v,lab)
		print "Estado actual: ", v
		print "Estados validos: ", adyacentes(v,lab)
		print "Estado sucesor: ", w
		print "Estado Empilado: ", w
		print "Pila: ", pila.lista
		r = raw_input(" ")
#--------------------------------------------------------

    return visitados
