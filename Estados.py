def arriba(actual):
    return (actual[0]-1, actual[1], "arriba")

def abajo(actual):
    return (actual[0]+1,actual[1],"abajo")

def izquierda(actual):
    return (actual[0],actual[1]-1,"izquierda")

def derecha(actual):
    return (actual[0],actual[1]+1,"derecha")

#actual es una tupla (i,j,movimiento)
def valido(actual,laberinto):
    #limite para las filas (i)
    if actual[0]<0 or actual[0]>len(laberinto)-1:
        return False
    #limite para las columnas (j)
    if actual[1]<0 or actual[1]>len(laberinto[0])-1:
        return False

    if laberinto[actual[0]][actual[1]] == '#':
        return False
    return True

def adyacentes(actual,laberinto):
    list = []
    if laberinto[actual[0]][actual[1]]=='#':
        return list
    est0 = abajo(actual)
    est1 = arriba(actual)
    est2 = izquierda(actual)
    est3 = derecha(actual)
    if valido(est0,laberinto):
        list.append(est0)
    if valido(est1,laberinto):
        list.append(est1)
    if valido(est2,laberinto):
        list.append(est2)
    if valido(est3,laberinto):
        list.append(est3)
    return list

def compare_To(p1,p2):
    if p1[0] == p2[0] and p1[1] == p2[1]:
        return True
    return False

def en_visitados(nodo,visitados):
    for x in visitados:
       if compare_To(nodo,x):
           return True
    return False



