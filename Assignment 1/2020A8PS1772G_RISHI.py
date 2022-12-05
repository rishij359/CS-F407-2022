from Graph_Creator import *
import numpy as np
import random
import matplotlib.pyplot as plt
import time
import os

def assign_weights_to_states(population, edges):
    weights = np.zeros(population.shape[0])
    
    k = 0
    for state in population:
        weights[k] = fitness_function(edges, state)
        if(weights[k] == 0):
            weights[k] = 0.0001
        k = k+1
    
    weights = weights/np.sum(weights)
    return weights


def fitness_function(edges, state): # Fitness function finds and returns the fitness of 'state' given the edges and returns the fitness.
    fitness = 0
    for i in range(0,50):
        for edge in edges:
            if(edge[0] == i or edge[1] == i):
                if(state[edge[0]] == state[edge[1]]):
                    fitness = fitness + 1
                    break
    
    fitness = 50 - fitness
    return(fitness)


def random_vertex_colour():
    arr = np.zeros((50),dtype=int)
    for i in range(0,50):
        arr[i] = random.randrange(0, 3, 1)
    return arr


def best_population_fitness(population, edges):
    fitness = np.zeros(population.shape[0])
    i = 0
    best_state = np.zeros(50)
    for state in population:
        fitness[i] = fitness_function(edges, state)
        i = i+1
    max_fitness = np.max(fitness)
    for state in population:
        if(fitness_function(edges, state) == max_fitness):
            best_state = state
    return max_fitness, best_state


def mutate(child):
    rand = random.randrange(0, 100, 1)
    if(rand<30):
        randindex = random.randrange(0, 50, 1)
        a = []
        for i in range(0,3):
            if(i == child[randindex]):
                continue
            a.append(i)
        child[randindex] = random.choice(a)
    return(child)


def reproduce(parent1, parent2):
    crossover_point = random.randrange(0,49,1)
    child1 = np.zeros(50, int)
    child2 = np.zeros(50, int)

    child1[0:crossover_point+1] = parent1[0:crossover_point+1]
    child1[crossover_point+1:] = parent2[crossover_point+1:]

    child2[0:crossover_point+1] = parent2[0:crossover_point+1]
    child2[crossover_point+1:] = parent1[crossover_point+1:]

    child1 = mutate(child1)
    child2 = mutate(child2)
    return child1,child2

        
def genetic(population, edges):

    gens = 1
    
    initiaL_time = time.time()
    best_state = np.zeros((50), int)
    best_fitness = 0
    best_fitness, best_state = best_population_fitness(population, edges)
    indices = (np.array(range(0,np.shape(population)[0]), int))
    
    while True:
        population2 = np.zeros(np.shape(population), int)
        weights = assign_weights_to_states(population, edges)
        
        for j in range(0, np.shape(population)[0], 2):
            
            parent_indices = random.choices(indices, weights, k=2)
            while(parent_indices[0] == parent_indices[1]):
                parent_indices = random.choices(indices, weights, k=2)
            population2[j], population2[j+1] = reproduce(population[parent_indices[0]] , population[parent_indices[1]])
         
        
        current_best_fitness, current_best_state = best_population_fitness(population2, edges)
        if(current_best_fitness>=best_fitness):
            best_fitness = current_best_fitness
            best_state = current_best_state
        population = population2

        gens +=1

        if(time.time()- initiaL_time>=44):
            break
        
        if(best_fitness == 50):
            break

    return(best_state, best_fitness, gens, time.time()- initiaL_time)

    
def main():
    gc = Graph_Creator()

    path = os.path.join("Testcases","200")
    edges = gc.ReadGraphfromCSVfile("50") # Reads the edges of the graph from a given CSV file from the Testcases folder

    population = np.zeros((150,50), int) # Defines a ppopulation of size 150.
    for i in range(0, 150):
        population[i] = random_vertex_colour()
    
    best_state,best_fitness ,gens, time_taken = genetic(population, edges)
    print("Roll no : 2020A8PS1772G")
    print("Number of edges :",np.shape(edges)[0])
    print("Best state :")
    colour= ['B', 'G', 'R']
    for i in range(0,50):
        if(i == 49):
            print(str(i)+":"+str(colour[best_state[i]]))
        
        else:
            print(str(i)+":"+str(colour[best_state[i]])+",", end = " ")
    print("Fitness value of best state :", best_fitness)
    print("Time taken :",round(time_taken, 2),"seconds")

    
    
    


if __name__=='__main__':
    main()


