import matplotlib.pyplot as plt
import math


# relación de valores a visualizar
grados = [i for i in range (-360, 361, 10)]
seno = [math.sin(math.radians(i)) for i in grados]
coseno = [math.cos(math.radians(i)) for i in grados]

# crear trazado en tres dimensiones
ax = plt.axes(projection='3d')

# dibujar los valores x, y, z
ax.plot(grados, seno, coseno, 'red')

# mostar el gráfico
plt.show()