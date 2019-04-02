#rellena el sudoku paso a paso de forma lenta solo se usa si es necesario y ya cuando se relleno la mayor cantidad 
# de espacios posibles

import arreglador
import resultor

def ponedor(x,puntos):
    
    nPunt = []
    arr = arreglador.arrg(x,puntos[0])
    
    while(True):
        
        if len(puntos) == 1 and len(arr) == 1 :
            x[puntos[0][0]][puntos[0][1]] = arr[0]
            return x
        elif not arr:
            x[puntos[0][0]][puntos[0][1]] = None
            return False
        else:
            num = arr.pop(0) 
            x[puntos[0][0]][puntos[0][1]] = num

            nPunt = resultor.res(x)
            xResuelta = ponedor(x,nPunt)
            
        if xResuelta:
            return xResuelta
