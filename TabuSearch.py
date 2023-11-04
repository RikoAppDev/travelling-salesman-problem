import random

import World


class TabuSearch:
    world: World
    final_permutation: list
    nearest_neighbour_value: float
    max_iterations = 1000
    max_tabu_list_size = 50
    max_none_improve = 100

    def __init__(self, world):
        self.world = world
        self.nearest_neighbour_value = world.get_permutation_value(world.nearest_neighbour_permutation)
        self.final_permutation = self.algo(world.places)

    def algo(self, permutation):
        random.shuffle(permutation)

        best = permutation
        best_candidate = permutation
        tabu_list = [permutation]
        none_improve = 0

        i = 0
        while not i == self.max_iterations:
            neighborhood = self.get_neighborhood(best_candidate)
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

    def get_neighborhood(self, permutation):
        neighbor = permutation[:]
        neighborhood = []

        function = random.choice([0, 1])
        if function == 0:
            neighborhood = self.generate_neighborhood(neighbor)
        elif function == 1:
            neighborhood = self.two_opt_neighborhood(neighbor)

        return neighborhood

    @staticmethod
    def generate_neighborhood(permutation):
        neighborhood = []
        for i in range(len(permutation)):
            for j in range(i + 1, len(permutation)):
                neighbor = permutation[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighborhood.append(neighbor)

        return neighborhood

    @staticmethod
    def two_opt_neighborhood(permutation):
        amount = len(permutation)
        neighborhood = []

        for i in range(amount - 1):
            for j in range(i + 1, amount):
                neighbor = permutation[:i] + list(reversed(permutation[i:j])) + permutation[j:]
                neighborhood.append(neighbor)

        return neighborhood
