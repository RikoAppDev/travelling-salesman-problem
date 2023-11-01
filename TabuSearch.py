import random

import World


class TabuSearch:
    world: World
    final_permutation: list
    nearest_neighbour_value: float
    max_iterations: int
    max_tabu_list_size: int
    max_none_improve: int

    def __init__(self, world, max_iterations, max_tabu_list_size=50, max_none_improve=100):
        self.world = world
        self.nearest_neighbour_value = world.get_permutation_value(world.nearest_neighbour_permutation)
        self.max_iterations = max_iterations
        self.max_tabu_list_size = max_tabu_list_size
        self.max_none_improve = max_none_improve
        self.final_permutation = self.algo(world.places)

    def algo(self, permutation):
        random.shuffle(permutation)

        best = permutation
        best_candidate = permutation
        tabu_list = [permutation]
        none_improve = 0

        i = 0
        while not i == self.max_iterations:
            neighborhood = self.generate_neighborhood(best_candidate)
            best_candidate = neighborhood[0]
            for candidate in neighborhood:
                if (not tabu_list.__contains__(candidate)) and (self.fitness(candidate) > self.fitness(best_candidate)):
                    best_candidate = candidate

            if self.fitness(best_candidate) > self.fitness(best):
                best = best_candidate
                none_improve = 0
            else:
                none_improve += 1

            tabu_list.append(best_candidate)
            if len(tabu_list) > self.max_tabu_list_size:
                tabu_list.pop(0)

            i += 1
            print(f"\rIteration: {i} ♻️\tTrip length: {self.world.get_permutation_value(best):.2f}km 📏", end="")

            if none_improve >= self.max_none_improve:
                break

        return best

    def fitness(self, permutation):
        return self.nearest_neighbour_value / self.world.get_permutation_value(permutation)

    @staticmethod
    def generate_neighborhood(permutation):
        neighborhood = []
        for i in range(len(permutation)):
            for j in range(i + 1, len(permutation)):
                neighbor = permutation[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighborhood.append(neighbor)

        return neighborhood
