
def crea_laberinto(stringLab):
    #Retira los saltos de linea
    lista = stringLab.split()
    #Corroboramos que todos los saltos de linea esten fuera
    lista = [ x[:-1] if x[-1] == "\n" else x for x in lista]
    #Separa los caracteres y los presenta en una lista de listas
    lista = [[ch for ch in x] for x in lista]
    #retornamos la lista de listas
    return lista

def impLab(laberinto):
    for x in laberinto:
        for y in x:
            if y =='.':
                print " ",
            else:
                print(y),
	print " "

def laberinto_archivo(nombre_archivo):
    archivo = open(nombre_archivo,'r')
    laberinto = " "
    for linea in archivo:
        laberinto+=linea

    return laberinto


