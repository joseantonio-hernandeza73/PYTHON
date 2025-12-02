import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# crear trazado en tres dimensiones
fig = plt.figure(figsize=(8,5))
gs = gridspec.GridSpec(nrows=2, ncols=3, figure=fig)
ax1 = fig.add_subplot(gs[0, 0], projection='3d')
ax2 = fig.add_subplot(gs[0, 1], projection='3d')
ax3 = fig.add_subplot(gs[0, 2], projection='3d')
ax4 = fig.add_subplot(gs[1, 0], projection='3d')
ax5 = fig.add_subplot(gs[1, 1], projection='3d')
ax6 = fig.add_subplot(gs[1, 2], projection='3d')

# etiquetar los ejes
for ax in fig.get_axes():
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])
    ax.text(0,0,0,'000')

# ajustar la posición de la cámara
ax2.view_init(5, None)
ax3.view_init(75, None)
ax4.view_init(25, None, 25)
ax5.view_init(None, 5)
ax6.view_init(None, 75)

# establecer títulos
ax1.set_title("Por defecto", color='red')
ax2.set_title("(5, None)", color='red')
ax3.set_title("(75, None)", color='red')
ax4.set_title("(25, None, 25)", color='red', y=-0.1)
ax5.set_title("(None, 5)", color='red', y=-0.1)
ax6.set_title("(None, 75)", color='red', y=-0.1)

# mostar el gráfico
plt.show()