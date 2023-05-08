from PSO.pso import pso
from PSO import pso
import numpy as np
import matplotlib.pyplot as plt


def draw_state(X: np.ndarray, V: np.ndarray, pbest: np.ndarray, gbest: np.ndarray) -> None:
    x, y = np.array(np.meshgrid(np.linspace(0,5,100), np.linspace(0,5,100)))
    z = pso.f(x, y)
    x_min = x.ravel()[z.argmin()]
    y_min = y.ravel()[z.argmin()]

    fig, ax = plt.subplots(figsize=(5,5))
    fig.set_tight_layout(True)
    img = ax.imshow(z, extent=[0, 5, 0, 5], origin='lower', cmap='viridis', alpha=0.5)
    fig.colorbar(img, ax=ax)
    ax.plot([x_min], [y_min], marker='x', markersize=5, color="white")
    contours = ax.contour(x, y, z, 10, colors='black', alpha=0.4)
    ax.clabel(contours, inline=True, fontsize=8, fmt="%.0f")
    pbest_plot = ax.scatter(pbest[0], pbest[1], marker='o', color='black', alpha=0.5)
    p_plot = ax.scatter(X[0], X[1], marker='o', color='blue', alpha=0.5)
    p_arrow = ax.quiver(X[0], X[1], V[0], V[1], color='blue', width=0.005, angles='xy', scale_units='xy', scale=1)
    gbest_plot = plt.scatter([gbest[0]], [gbest[1]], marker='*', s=100, color='black', alpha=0.4)
    ax.set_xlim([0,5])
    ax.set_ylim([0,5])
    plt.savefig('current_state')