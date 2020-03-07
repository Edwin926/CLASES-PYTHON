# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:28:44 2019

@author: UPS

TEST DE VELICIDAD
"""
import numpy as np
import time
 
SIZE = 1000000
 
L1= range(SIZE)
L2= range(SIZE)
A1= np.arange(SIZE)
A2=np.arange(SIZE)
print ("\n"*1)
print ("RESULTADO USANDO LISTAS/TUPLAS EN PYTHON")
start= time.time()
result=[(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000)
print ("\n"*2)
print ("RESULTADO USANDO NUMPY")
start=time.time()
result= A1+A2
print((time.time()-start)*1000)

# matrices


import numpy as np

array=np.array([(1,2,3,4], [5,6,7,8]], dtype=np.int64)
print(array)

unos=np.ones((3,4))
print(unos)

ceros=np.zeros((3,4))
print(ceros)

aleatorio=np.random.random((2,2))
print(aleatorio)

vacia=np.empty((3,2))
print(vacia)

full=np.full((100,100),10)
print(full)

espacio1=np.arange(0,30,5)
print(espacio1)

espacio1=np.arange(0,30+1,5)
print(espacio1)

espacio2=np.linspace(0,2,5)
print(espacio2)

espacio2=np.linspace(0,2,10)
print(espacio2)


espacio2=np.linspace(0,2,100)
print(espacio2)





























