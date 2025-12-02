import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


# obtener datos a trazar
X, Y, Z = axes3d.get_test_data(0.053)

# crear trazado en tres dimensiones
ax = plt.axes(projection='3d')

# dibujar los valores
ax.plot_wireframe(X, Y, Z, rstride=7, cstride=7)
ax.plot_wireframe(X, Y, Z, rcount=3, ccount=3, color='b')

# mostar el gráfico
plt.show()