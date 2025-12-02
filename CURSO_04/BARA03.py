import matplotlib.pyplot as plt


# crear trazado en tres dimensiones
ax = plt.axes(projection='3d')

# etiquetar los ejes
ax.set_xlabel("Eje X", color='red')
ax.set_ylabel("Eje Y", color='red')
ax.set_zlabel("Eje Z", color='red')

# establecer título 
ax.set_title("Ejes en 3D", color='red')

# mostar el gráfico
plt.show()