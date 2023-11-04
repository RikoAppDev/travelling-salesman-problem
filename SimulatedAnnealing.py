import math
import random

import World


class SimulatedAnnealing:
    world: World
    final_permutation: list
    nearest_neighbour_value: float
    max_none_improve: int
    alpha = 0.999
    temperature = 1

    def __init__(self, world):
        self.world = world
        self.nearest_neighbour_value = world.get_permutation_value(world.nearest_neighbour_permutation)
        self.max_none_improve = len(world.places) * int(10 * math.pi)
        self.final_permutation = self.algo(world.places)

    def algo(self, permutation):
        random.shuffle(permutation)

        best = permutation
        none_improve = 0

        i = 0
        while none_improve < self.max_none_improve:
            best_candidate = self.get_neighbor(best)

            if self.fitness(best_candidate) > self.fitness(best):
                best = best_candidate
                none_improve = 0
            elif self.fitness(best_candidate) == self.fitness(best):
                best = best_candidate
                none_improve += 1
            else:
                possibility = math.exp((self.fitness(best_candidate) - self.fitness(best)) / float(self.temperature))
                if random.uniform(0, 1) <= possibility:
                    best = best_candidate
                    none_improve = 0
                else:
                    none_improve += 1

            self.temperature *= self.alpha

            i += 1
            print(
                f"\rIteration: {i + 1} ♻️\tTrip length: {self.world.get_permutation_value(best):.2f}km 📏\tTemperature: {self.temperature} 🌡️",
                end=""
            )

        return best

    def fitness(self, permutation):
        return self.nearest_neighbour_value / self.world.get_permutation_value(permutation)

    def get_neighbor(self, permutation):
        neighbor = permutation[:]

        function = random.choice([0, 1, 2, 3, 4])
        if function == 0:
            neighbor = self.swap(neighbor)
        elif function == 1:
            neighbor = self.insertion(neighbor)
        elif function == 2:
            neighbor = self.reordering(neighbor)
        elif function == 3:
            neighbor = self.reverse(neighbor)
        else:
            neighbor = self.transport(neighbor)

        return neighbor

    @staticmethod
    def swap(permutation):
        i, j = random.sample(range(len(permutation)), 2)
        permutation[i], permutation[j] = permutation[j], permutation[i]
        return permutation

    @staticmethod
    def insertion(permutation):
        i, j = random.sample(range(len(permutation)), 2)
        place = permutation.pop(i)
        permutation.insert(j, place)
        return permutation

    @staticmethod
    def reordering(permutation):
        i, j = sorted(random.sample(range(len(permutation)), 2))
        subsequence = permutation[i:j + 1]
        random.shuffle(subsequence)
        return permutation[:i] + subsequence + permutation[j + 1:]

    @staticmethod
    def reverse(permutation):
        start = random.randint(0, len(permutation) - 1)
        end = random.randint(start, len(permutation) - 1)
        return permutation[:start] + list(reversed(permutation[start:end + 1])) + permutation[end + 1:]

    @staticmethod
    def transport(permutation):
        i, j = sorted(random.sample(range(len(permutation)), 2))
        insert_position = random.randint(0, len(permutation))
        subsequence = permutation[i:j + 1]
        permutation = permutation[:i] + permutation[j + 1:]
        return permutation[:insert_position] + subsequence + permutation[insert_position:]
