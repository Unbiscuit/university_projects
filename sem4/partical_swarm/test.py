from PSO import pso
import numpy as np
import matplotlib.pyplot as plt

def main():
    n_particles = 20

    x, y = np.array(np.meshgrid(np.linspace(0,5,100), np.linspace(0,5,100)))
    z = pso.f(x, y)
    x_min = x.ravel()[z.argmin()]
    y_min = y.ravel()[z.argmin()]

    X = np.random.rand(2, n_particles) * 5
    V = np.random.randn(2, n_particles) * 0.1
    pbest = X
    pbest_obj = pso.f(X[0], X[1])
    gbest = pbest[:, pbest_obj.argmin()]

    fig, ax = plt.subplots(figsize=(8,6))
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

if __name__ == "__main__":
    main()