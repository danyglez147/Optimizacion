import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return pow(x,4)

def f_1a(x):
  return 4*pow(x,3)
def f_2a(x):
  return (12*pow(x,2))

print("La funcion es concava en f(x)=x a la cuarta  a partir de esta figura y es obvio que la gráfica es cóncava hacia arriba si x=0. Matematicas aplicadas Frank S. Budnick")

#La gráfica de una función f es cóncava hacia arriba (hacia abajo) en un intervalo
# si f aumenta (disminuye) en todo ese intervalo.
# Si la función es 2 veces derivable, ésta es cóncava si f"(x) < 0


# Grafica
x=np.arange(-3,3.1,0.1)
plt.subplot(1,1,1)
plt.plot(x,f(x))   