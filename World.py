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
            if (a_place.get("lat") - PLACE_DIAMETER - 5 < x < a_place.get("lat") + PLACE_DIAMETER + 5 and
                    a_place.get("long") - PLACE_DIAMETER - 5 < y < a_place.get("long") + PLACE_DIAMETER + 5):
                return True

        return False

    def generate_places(self, count: int):
        w_places = []
        total = count

        while count != 0:
            count -= 1
            print(f"\rGenerating world: loading {((total - count) * 100 / total) - 0.1:.02f} %", end="")

            w_place: dict = {}
            x = random.randint(5, WINDOW_WIDTH - (PLACE_DIAMETER + 5))
            y = random.randint(5, WINDOW_HEIGHT - (PLACE_DIAMETER + 5))

            if self.check_place_collision(x, y, w_places):
                count += 1
                continue

            w_place.setdefault("lat", x)
            w_place.setdefault("long", y)
            w_places.append(w_place)

        return w_places

    def calculate_distance(self, place1, place2):
        dx = place2.get("lat") - place1.get("lat")
        dy = place2.get("long") - place1.get("long")

        return math.sqrt(dx * dx + dy * dy)
