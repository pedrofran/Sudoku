# coding: utf-8
# Your code here!

import arreglador
import resultor
import ponedor
#sudoku se debe rellenar con None los espacios
x = [[None,None,None,None,None,6,None,None,7],
    [4,2,None,None,5,None,None,8,None],
    [None,3,None,None,8,None,None,None,6],
    [2,None,4,None,None,8,1,7,None],
    [None,None,7,3,None,2,4,None,None],
    [None,1,9,4,None,None,8,None,2],
    [1,None,None,None,6,None,None,2,None],
    [None,7,None,None,4,None,None,3,9],
    [5,None,None,2,None,None,None,None,None]]


#arreglo de puntos huecos
puntos = resultor.res(x)

#rellena los espacios con una sola posibilidad 
ent= True
  
while(True):
    ent = True
    for y in puntos:
        if len(arreglador.arrg(x,y))==1:
            x[y[0]][y[1]] = arreglador.arrg(x,y)[0]
            ent=False
        
    puntos = resultor.res(x)
    if ent:        
        break
  
# rellenador lento  
if puntos:
    x = ponedor.ponedor(x,puntos)
    
if x:
    #print final del sudoku
    print("sudoku Resuelto:")
    for a in x:
        print(*a, sep=" ")
else:
    print("el sudoku es imposible")
    



    