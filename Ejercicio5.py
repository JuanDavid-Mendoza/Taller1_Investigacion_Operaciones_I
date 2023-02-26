from matplotlib import pyplot as plt
import numpy as np

# Funciones a graficar (Restricciones)
f = lambda x: 20 - (2/3)*x

# Valores del eje x
x = np.linspace(0, 30, 30)

plt.plot(x,f(x),'b',label="y= 20 - (2/3)x") # Graficar función
plt.plot(np.full(31,0.1),np.array(range(0,31)),'k',label="x= 0") # Graficar eje y
plt.plot(x,np.full(30,0.1),'k',label="y= 0") # Graficar eje x
plt.fill_between(x, 30, f(x), color="#cccaca") # Sombrear región entre y=30 y y=función

plt.title('Ejercicio 5') # Título de la gráfica
plt.xlabel("Eje X") # Título del eje horizontal
plt.ylabel("Eje Y") # Título del eje vertical
plt.legend(loc=1) # Nombre de las funciones
plt.grid() # Cuadricula

plt.ylim(0, 30) # Límites del eje y
plt.xlim(0, 30) # Límites del eje x
plt.yticks(np.array(range(0,31,5))) # Escala del eje y
plt.xticks(np.array(range(0,31,5))) # Escala del eje x

plt.show() # Mostrar gráfico