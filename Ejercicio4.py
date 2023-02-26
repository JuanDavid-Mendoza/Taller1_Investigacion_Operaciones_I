from matplotlib import pyplot as plt
import numpy as np

# Funciones a graficar (Restricciones)
f = lambda x: 3 - 2*x
g = lambda x: x

# Valores del eje x
x = np.linspace(0, 6, 6)

plt.plot(x,f(x),'b',label="y= 3 - 2x",linestyle="--") # Graficar función
plt.plot(x,g(x),'r',label="y= x") # Graficar función
plt.plot(x,np.full(6,0.5),'g',label="y= 1/2",linestyle="--") # Graficar función horizontal
plt.fill_between(x, 0, f(x), color="#cccaca") # Sombrear región entre y=0 y y=función
plt.fill_between(x, 6, g(x), color="#cccaca") # Sombrear región entre y=6 y y=función
plt.fill_between(x, 0, np.full(6,0.5), color="#cccaca") # Sombrear región entre y=0 y y=función

plt.title('Ejercicio 4') # Título de la gráfica
plt.xlabel("Eje X") # Título del eje horizontal
plt.ylabel("Eje Y") # Título del eje vertical
plt.legend(loc=1) # Nombre de las funciones
plt.grid() # Cuadricula

plt.ylim(0, 6) # Límites del eje y
plt.xlim(0, 6) # Límites del eje x
plt.yticks(np.array(range(0,7))) # Escala del eje y
plt.xticks(np.array(range(0,7))) # Escala del eje x

plt.show() # Mostrar gráfico