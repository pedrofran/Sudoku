# coding: utf-8
# Your code here!

import arreglador
import resultor
import comprobador

x =[[2,None,5,9,3,8,4,6,7],
[7,8,6,1,2,4,3,5,9],
[9,3,4,6,5,7,2,8,1],
[8,6,9,5,None,2,1,7,3],
[None,4,3,7,8,6,5,9,2],
[5,2,7,3,9,1,8,4,6],
[6,7,2,4,1,5,9,3,8],
[4,9,8,2,6,3,7,1,5],
[3,5,1,8,7,9,6,2,None]]



puntos = resultor.res(x)
relleno = [None] * len(puntos)
ent= True

print(relleno,puntos)
    
while(True):
    for y in puntos:
        ent = True
        if len(arreglador.arrg(x,y))==1:
            x[y[0]][y[1]] = arreglador.arrg(x,y)[0]
            ent=False
    if ent:        
        break
        
        
comprobador.comp(x)    
