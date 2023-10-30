import math
import random
from constants import *


class World:
    places = []

    def __init__(self, amount):
        self.places = self.generate_places(int(amount))

    @staticmethod
    def check_place_collision(x, y, actual_places: list):
        for a_place in actual_places:
            if (a_place.get("lat") - PLACE_DIAMETER - GAP < x < a_place.get("lat") + PLACE_DIAMETER + GAP and
                    a_place.get("long") - PLACE_DIAMETER - GAP < y < a_place.get("long") + PLACE_DIAMETER + GAP):
                return True

        return False

    def generate_places(self, count: int):
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

            w_place.setdefault("lat", x)
            w_place.setdefault("long", y)
            w_places.append(w_place)

        return w_places

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
