from Estados import adyacentes
from Split import crea_laberinto, laberinto_archivo
from DFS import search_DFS
from BFS import search_BFS
from run_laberinto import run_lab

laberinto = laberinto_archivo('laberinto.txt')
inicial = (61,0,)

lab = crea_laberinto(laberinto)

#visitados = search_DFS(inicial,laberinto)
visitados = search_BFS(inicial,laberinto)
