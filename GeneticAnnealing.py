import random
import math

# Define parameters
population_size = 100
mutation_rate = 0.1
crossover_rate = 0.8
max_iterations = 1000
chromosome_length = 10  # Adjust according to your problem domain

# Define objective function
def objective_function(chromosome):
    return sum(x**2 for x in chromosome)  # Example function (minimize)

# Initialize population
population = [[random.uniform(-10, 10) for _ in range(chromosome_length)] for _ in range(population_size)]

# Main loop
for iteration in range(max_iterations):
    # Evaluate fitness
    fitness_values = [objective_function(chromosome) for chromosome in population]
    
    # Select parents
    parents = random.choices(population, weights=fitness_values, k=2)
    
    # Crossover
    if random.random() < crossover_rate:
        crossover_point = random.randint(1, chromosome_length - 1)
        offspring = parents[0][:crossover_point] + parents[1][crossover_point:]
    else:
        offspring = parents[0][:]
    
    # Mutation
    if random.random() < mutation_rate:
        mutation_index = random.randint(0, chromosome_length - 1)
        offspring[mutation_index] += random.uniform(-0.1, 0.1)
    
    # Annealing operation
    temperature = 1.0 / math.log(iteration + 2)
    delta_fitness = objective_function(offspring) - objective_function(parents[0])
    if delta_fitness < 0 or random.random() < math.exp(-delta_fitness / temperature):
        population[random.randint(0, population_size - 1)] = offspring

# Find the best solution
best_solution = min(population, key=objective_function)
best_fitness = objective_function(best_solution)

print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)
