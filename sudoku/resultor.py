#se encarga de buscar los huecos en el sudoku y mandar un arreglo con sus posiciones
import arreglador
def res(x):
    
    sal = True
    cont=0
    huecos =[]
    
    for a in range(9):
        for c in range(9):
            
            if x[a][c] is None:
                huecos.append([a,c])
        
    return(huecos)   
