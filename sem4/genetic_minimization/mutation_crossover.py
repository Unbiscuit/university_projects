import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from GA import GA

def main():
    x = []   
    y = []
    z = []
    for i in range(1, 101, 4):
        for j in range(1, 101, 4):
            population = GA.GA(100, i/100, j/100, -10, 10)
            for k in range(3):
                population.tournament5()
                population.crossover()
                population.mutation(-10, 10)
                population.recalculate_fitness()
            x.append(i)
            y.append(j)
            z.append(np.abs(population.get_population()[0][2]))

        print(i)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.array(x)
    y = np.array(y)
    z = np.array(z)

    ax.scatter(x, y, z)

    ax.set_xlabel('crossover chance %')
    ax.set_ylabel('mutation chance %')
    ax.set_zlabel('absolute value fitness after 3 steps')

    ax.set_title('dependence of fitness on mutation and crossover')
                
    plt.show()


if __name__ == "__main__":
    main()