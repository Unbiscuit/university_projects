import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from GA import GA

def main():
    x = []   
    y = []
    for i in range(1, 300):
        population = GA.GA(i, 0.2, 0.60, -10, 10)
        for k in range(3):
            population.tournament5()
            population.crossover()
            population.mutation(-10, 10)
            population.recalculate_fitness()
        x.append(i)
        y.append(np.abs(population.get_population()[0][2]))

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    x = np.array(x)
    y = np.array(y)

    ax.plot(x, y)

    ax.set_xlabel('population size')
    ax.set_ylabel('absolute value fitness after 3 steps')

    ax.set_title('dependence of fitness on mutation and crossover')
                
    plt.show()


if __name__ == "__main__":
    main()