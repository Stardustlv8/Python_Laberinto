from Split import impLab

def run_lab(visitado, laberinto):
    laberinto[visitado[0]][visitado[1]]='*'
    impLab(laberinto)

