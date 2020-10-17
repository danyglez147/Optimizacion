import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return pow(x,4)/12-pow(x,3)/2+pow(x,2)+10

def f_1a(x):
  return pow(x,3)/3-3*pow(x,2)/2+2*x
def f_2a(x):
  return pow(x,2)-3*x+2


print(f_2a(0.9))
print(f_2a(1.1))
print("Punto inflexion en x=1")
print(f_2a(1.9))
print(f_2a(2.1))
print("Punto inflexion en x=2")

#Son puntos de inflexion debido a que el signo cambia en ambos resultados donde la funcion se evalua en x=0.9 y x=1.1 para el caso de x=1; 
# y ademas en x=1.9 y x=2.1 para x=2 respectivamente

    
# Grafica
x=np.arange(-3,3.1,0.1)
punto=f(1)
plt.plot(1,punto, marker=".", color="green")
punto=f(2)
plt.plot(2,punto, marker=".", color="green")
plt.subplot(1,1,1)
plt.plot(x,f(x)) 

