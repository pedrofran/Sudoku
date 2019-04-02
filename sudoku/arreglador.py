#consigue los posibles numeros que pueden ir en un espacio

#para colocar el punto en el lugar adecuado para la verificacion en cuadrado
def posicionador(punto):  
    if punto<3:
        return 0
    elif punto<6:
        return 3
    else:     
        return 6


def arrg(x,punt):
    arr = []
    pos =[0,0]
    
#asignacion de puntos para el cuadrado
    pos[0],pos[1] = posicionador(punt[0]),posicionador(punt[1])

  #revision horizontal y vertical
    for a in range(9):
        if  x[punt[0]][a] not in arr and x[punt[0]][a] is not None:
            arr.append(x[punt[0]][a])
        
        if not x[a][punt[1]] in arr and x[a][punt[1]] is not None:                
            arr.append(x[a][punt[1]])
#revision cuadrada            
    for suma1 in range(3):
            for suma2 in range(3):
                if not x[pos[1]+suma1][pos[0]+suma2] in arr and x[pos[0]+suma1][pos[1]+suma2] is not None:
                    arr.append(x[pos[0]+suma1][pos[1]+suma2])

    arrF= []        
    for numb in range(1,10):

        if numb not in arr:
            arrF.append(numb)

    
    return sorted(arrF)