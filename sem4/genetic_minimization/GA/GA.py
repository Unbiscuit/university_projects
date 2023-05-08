import numpy as np
import random
from GA import converters 


class GA:

    __population = {}
    # create initial population with given parametrs
    def __init__(self, population_size: int, crossover_probability: float, mutation_probability: float, lower_bound: float, upper_bound: float):
        self.population_size = population_size
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability

        population = {}
        for i in range(self.population_size):
            x1 = random.uniform(lower_bound, upper_bound)
            x2 = random.uniform(lower_bound, upper_bound)
            fit = self._fitness(x1, x2)
            x1 = converters.float_to_bin(x1)
            x2 = converters.float_to_bin(x2)
            genotype = str(x1) + str(x2)
            population[i] = {"x1x2": genotype, "fitness":fit}
        self.__population = population

    # equation which needs to be minimized 
    def _equation(self, x1: float, x2: float):
        equation = -12*x2 + 4*np.power(x1, 2) + 4*np.power(x2, 2) - 4*x1*x2
        return equation
    
    # evaluate fitness
    def _fitness(self, x1: float, x2: float):
        fitness = self._equation(x1, x2)
        return fitness

    # selection using tournament of 5
    def tournament5(self):
        for i in range(self.population_size):
            participant = self.__population[random.randint(0,self.population_size-1)]
            winner_number = participant["x1x2"]
            winner_fitness = participant["fitness"]
            for j in range(4):
                participant = self.__population[random.randint(0,self.population_size-1)]
                if participant["fitness"] < winner_fitness:
                    winner_fitness = participant["fitness"]
                    winner_number = participant["x1x2"]

            self.__population[i] = {"x1x2":winner_number, "fitness":winner_fitness}

    # crossover with 1 dot
    def crossover(self):
        pivot = int(self.population_size/2)
        for i in range(pivot):
            pare_probability = random.uniform(0, 1)
            if pare_probability > self.crossover_probability:
                specimen1 = self.__population[i]["x1x2"]
                specimen2 = self.__population[i + pivot]["x1x2"]
                crossover1 = specimen1[0:32] + specimen2[32:64]
                crossover2 = specimen2[0:32] + specimen1[32:64]
                self.__population[i]["x1x2"] = crossover1
                self.__population[i + pivot]["x1x2"] = crossover2

    # mutation; if new gens not in given range not mutate
    def mutation(self, lower_bound: float, upper_bound: float):
        for i in range(self.population_size):
            specimen = self.__population[i]["x1x2"]
            new_specimen = ''
            for bit in specimen:
                mutation_stability = random.uniform(0, 1)
                if mutation_stability < self.mutation_probability:
                    if bit == '1':
                        new_specimen += '0'
                    else:
                        new_specimen += '1'
                else:
                    new_specimen += bit
            
            x1 = converters.bin_to_float(new_specimen[0:32])
            x2 = converters.bin_to_float(new_specimen[32:64])
            if lower_bound <= x1 <= upper_bound and lower_bound <= x2 <= upper_bound:
                self.__population[i]["x1x2"] = new_specimen

    # recalculate fitness after all stages
    def recalculate_fitness(self):
        for i in range(self.population_size):
            specimens_genotype = self.__population[i]["x1x2"]
            natural_x1 = converters.bin_to_float(specimens_genotype[0:32])
            natural_x2 = converters.bin_to_float(specimens_genotype[32:64])
            fit = self._fitness(natural_x1, natural_x2)
            self.__population[i]["fitness"] = fit

    # get list of current population
    def get_population(self):
        list_of_results = []
        for i in range(self.population_size):
            line = self.__population[i]["x1x2"]
            x1 = converters.bin_to_float(line[0:32])
            x2 = converters.bin_to_float(line[32:64])
            fit = self.__population[i]["fitness"]
            list_of_results.append([x1, x2, fit])

        list_of_results = sorted(list_of_results, key=lambda fit: fit[2]) 

        return list_of_results
