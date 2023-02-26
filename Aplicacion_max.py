from matplotlib import pyplot as plt
import numpy as np

# Funciones a graficar (Restricciones)
f = lambda x: 200 - (2/3)*x
g = lambda x: 500 - x
h = lambda x: 400 - 2*x

# Valores del eje x
x = np.linspace(0, 500, 500)

plt.plot(x,f(x),'b',label="y= 200 - (2/3)x") # Graficar función
plt.plot(x,g(x),'g',label="y= 500 - x") # Graficar función
plt.plot(x,h(x),'r',label="y= 400 - 2x") # Graficar función
plt.plot(np.full(501,2),np.array(range(0,501)),'k',label="x= 0") # Graficar eje y
plt.plot(x,np.full(500,1),'k',label="y= 0") # Graficar eje x
plt.fill_between(x, 500, f(x), color="#cccaca") # Sombrear región entre y=500 y y=función
plt.fill_between(x, 500, g(x), color="#cccaca") # Sombrear región entre y=500 y y=función
plt.fill_between(x, 500, h(x), color="#cccaca") # Sombrear región entre y=500 y y=función

plt.title('Ejercicio Aplicación - Maximizar') # Título de la gráfica
plt.xlabel("Eje X") # Título del eje horizontal
plt.ylabel("Eje Y") # Título del eje vertical
plt.legend(loc=1) # Nombre de las funciones
plt.grid() # Cuadricula

plt.ylim(0, 500) # Límites del eje y
plt.xlim(0, 500) # Límites del eje x
plt.yticks(np.array(range(0,501,100))) # Escala del eje y
plt.xticks(np.array(range(0,501,100))) # Escala del eje x

plt.show() # Mostrar gráfico