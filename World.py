import math
import random
from constants import *


class World:
    places: list
    distance_matrix: list[list]
    nearest_neighbour_permutation: list

    def __init__(self, amount, seed):
        self.places = self.generate_places(int(amount), seed)
        self.distance_matrix = self.fill_distance_matrix()
        self.nearest_neighbour_permutation = self.get_nearest_neighbour()

    @staticmethod
    def check_place_collision(x, y, actual_places: list):
        for a_place in actual_places:
            if (a_place.get("lat") - PLACE_DIAMETER - GAP < x < a_place.get("lat") + PLACE_DIAMETER + GAP and
                    a_place.get("long") - PLACE_DIAMETER - GAP < y < a_place.get("long") + PLACE_DIAMETER + GAP):
                return True

        return False

    def generate_places(self, count: int, seed: int):
        random.seed(seed)
        w_places = []
        total = count

        while count != 0:
            count -= 1
            print(f"\rGenerating world: loading {((total - count) * 100 / total) - 0.1:.02f} %", end="")

            w_place: dict = {}
            x = random.randint(GAP, WINDOW_WIDTH - (PLACE_DIAMETER + GAP))
            y = random.randint(GAP, WINDOW_HEIGHT - (PLACE_DIAMETER + GAP))

            if self.check_place_collision(x, y, w_places):
                count += 1
                continue

            w_place.setdefault("id", "uid" + str(total - count - 1))
            w_place.setdefault("lat", x)
            w_place.setdefault("long", y)
            w_places.append(w_place)

        print(f"\rGenerating world: loading 100% ✅", end="")
        return w_places

    def fill_distance_matrix(self):
        distance_matrix = []

        for p1 in self.places:
            distances = []
            for p2 in self.places:
                distances.append(self.calculate_distance(p1, p2))

            distance_matrix.append(distances)

        return distance_matrix

    @staticmethod
    def calculate_distance(place1, place2):
        dx = place2.get("lat") - place1.get("lat")
        dy = place2.get("long") - place1.get("long")

        return math.sqrt(dx * dx + dy * dy)

    def get_permutation_value(self, permutation):
        value = 0
        amount = len(permutation)

        for i in range(amount - 1):
            value += self.calculate_distance(permutation[i], permutation[i + 1])

        value += self.calculate_distance(permutation[amount - 1], permutation[0])

        return value

    def get_nearest_neighbour(self):
        start_place = random.randint(0, len(self.places) - 1)
        permutation = [self.get_place_with_uid(start_place)]

        visited = []
        actual_place = start_place
        while len(permutation) != len(self.places):
            minimum = max(self.distance_matrix[actual_place])

            index = 0
            for distance in self.distance_matrix[actual_place]:
                if index != actual_place and self.get_place_with_uid(index) not in permutation and distance < minimum:
                    actual_place = index
                    minimum = distance
                index += 1

            visited.append(actual_place)
            permutation.append(self.get_place_with_uid(actual_place))

        return permutation

    def get_place_with_uid(self, n):
        for p in self.places:
            if p.get("id") == "uid" + str(n):
                return p
