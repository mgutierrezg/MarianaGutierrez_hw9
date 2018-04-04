import numpy as np
import matplotlib.pyplot as plt

# Cragamos los tiempos de python 
losdepy = np.loadtxt("times_python.csv")

#Cargamos los tiempos de c++
losdec =  np.loadtxt("times_cpp.csv")

#para la grafica separamos las columnas
x1 = losdepy[:,0]
x2 = losdec[:,0]

y1 = losdepy[:,1]
y2 = losdepy[:,1]

a = plt.plot(x1,y1, c = "m")
b = plt.plot(x2,y2, c = "c")

plt.xlabel("N")
plt.ylabel("Tiempo")
plt.legend([a,b] , ["Python","C++"])
plt.savefig("cpp_vs_python.png")

