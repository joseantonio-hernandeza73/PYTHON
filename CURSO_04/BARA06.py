import matplotlib.pyplot as plt
import random


# relación de valores a visualizar
x = [i for i in range(-10, 20)]
y = random.sample(x, k=30)
z = random.sample(y, k=30)

x2 = [i for i in range(-20, 10)]
y2 = random.sample(x2, k=30)
z2 = random.sample(y2, k=30)

# crear trazado en tres dimensiones
ax = plt.axes(projection='3d')

# dibujar los valores
ax.scatter3D(x, y, z, c='g', marker='o')
ax.scatter3D(x2, y2, z2, c ='r', marker='*')

# mostar el gráfico
plt.show()