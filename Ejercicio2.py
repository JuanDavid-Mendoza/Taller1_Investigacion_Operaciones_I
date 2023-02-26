from matplotlib import pyplot as plt
import numpy as np

# Valores del eje x
x = np.linspace(0, 6, 6)

plt.plot(x,np.full(6,5),'b',label="y= 5") # Graficar función horizontal
plt.fill_between(x, 6, np.full(6,5), color="#cccaca") # Sombrear región entre y=6 y y=función

plt.title('Ejercicio 2') # Título de la gráfica
plt.xlabel("Eje X") # Título del eje horizontal
plt.ylabel("Eje Y") # Título del eje vertical
plt.legend(loc=1) # Nombre de las funciones
plt.grid() # Cuadricula

plt.ylim(0, 6) # Límites del eje y
plt.xlim(0, 6) # Límites del eje x
plt.yticks(np.array(range(0,7))) # Escala del eje y
plt.xticks(np.array(range(0,7))) # Escala del eje x

plt.show() # Mostrar gráfico