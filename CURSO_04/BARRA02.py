import matplotlib.pyplot as plt
import numpy as np

# 1. Crear figura y ejes 3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# 2. Crear datos
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# 3. Graficar la superficie
ax.plot_surface(X, Y, Z, cmap='viridis')

# 4. Personalizar y mostrar
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
plt.title('Superficie 3D')
plt.show()