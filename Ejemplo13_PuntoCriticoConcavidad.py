import numpy as np
import matplotlib.pyplot as plt

def f(x):
   return x*x*x*x /4 - 9 * x*x/2
def f_1a(x):
  return x*x*x-9(x)
def f_2a(x):
  return 3*(x*x)-9

x=np.arange(-4,4.1,0.1)  
for dato in x:
  if dato<3:
      if dato<-3:
          print("Funcion Concava hacia arriba",dato)
      if dato>-3:
          print("Funcion Concava hacia abajo",dato)
  else:
      print(" Funcion Concava hacia arriba",dato)
      
#Grafica   
 
punto=f(-3)
plt.plot(3,punto, marker="o", color="green")
punto=f(3)
plt.plot(-3,punto, marker="o", color="green")
plt.subplot(1,1,1)
plt.plot(x,f(x)) 
