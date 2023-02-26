from matplotlib import pyplot as plt
import numpy as np

# Funciones a graficar (Restricciones)
f = lambda x: 180 - 2*x
g = lambda x: 80 - x/2
h = lambda x: 100 - x

# Valores del eje x
x = np.linspace(0, 200, 200)

plt.plot(x,f(x),'b',label="y= 180 - 2x") # Graficar función
plt.plot(x,g(x),'g',label="y= 80 - x/2") # Graficar función
plt.plot(x,h(x),'r',label="y= 100 - x") # Graficar función
plt.plot(np.full(201,1),np.array(range(0,201)),'k',label="x= 0") # Graficar eje y
plt.plot(x,np.full(200,0.5),'k',label="y= 0")  # Graficar eje x
plt.fill_between(x, 200, f(x), color="#cccaca") # Sombrear región entre y=200 y y=función
plt.fill_between(x, 200, g(x), color="#cccaca") # Sombrear región entre y=200 y y=función
plt.fill_between(x, 200, h(x), color="#cccaca") # Sombrear región entre y=200 y y=función

plt.title('Ejercicio 6') # Título de la gráfica
plt.xlabel("Eje X") # Título del eje horizontal
plt.ylabel("Eje Y") # Título del eje vertical
plt.legend(loc=1) # Nombre de las funciones
plt.grid() # Cuadricula

plt.ylim(0, 200) # Límites del eje y
plt.xlim(0, 200) # Límites del eje x
plt.yticks(np.array(range(0,201,20))) # Escala del eje y
plt.xticks(np.array(range(0,201,20))) # Escala del eje x

plt.show() # Mostrar gráfico