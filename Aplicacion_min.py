from matplotlib import pyplot as plt
import numpy as np

# Funciones a graficar (Restricciones)
f = lambda x: 3 - x/5
g = lambda x: 15 - 5*x

# Valores del eje x
x = np.linspace(0, 15, 15)

plt.plot(x,f(x),'b',label="y= 3 - x/5") # Graficar función
plt.plot(x,g(x),'g',label="y= 15 - 5x") # Graficar función
plt.plot(np.full(16,0.05),np.array(range(0,16)),'k',label="x= 0") # Graficar eje y
plt.plot(x,np.full(15,0.01),'k',label="y= 0") # Graficar eje x
plt.fill_between(x, 0, f(x), color="#cccaca") # Sombrear región entre y=0 y y=función
plt.fill_between(x, 0, g(x), color="#cccaca") # Sombrear región entre y=0 y y=función

plt.title('Ejercicio Aplicación - Minimizar') # Título de la gráfica
plt.xlabel("Eje X") # Título del eje horizontal
plt.ylabel("Eje Y") # Título del eje vertical
plt.legend(loc=1) # Nombre de las funciones
plt.grid() # Cuadricula

plt.ylim(0, 15) # Límites del eje y
plt.xlim(0, 15) # Límites del eje x
plt.yticks(np.array(range(0,16,3))) # Escala del eje y
plt.xticks(np.array(range(0,16,3))) # Escala del eje x

plt.show() # Mostrar gráfico