from time import sleep
from tkinter import *

from World import World
from constants import *


def connect_places(p1, p2, w_map):
    w_map.tag_lower(w_map.create_line(p1.get("lat") + PLACE_DIAMETER / 2, p1.get("long") + PLACE_DIAMETER / 2,
                                      p2.get("lat") + PLACE_DIAMETER / 2,
                                      p2.get("long") + PLACE_DIAMETER / 2,
                                      width=1, fill="black"))


def show_place(place, w_map, c):
    w_map.create_oval(place.get("lat"), place.get("long"), place.get("lat") + PLACE_DIAMETER,
                      place.get("long") + PLACE_DIAMETER,
                      outline="black", fill="red")
    w_map.create_text(place.get("lat") + PLACE_DIAMETER / 2, place.get("long") + PLACE_DIAMETER / 2, text=c,
                      fill="black",
                      font='"Comic Sans MS" 10 normal')


def show_best_trip(permutation, w_map):
    count = len(permutation)

    for j in range(count - 1):
        connect_places(permutation[j], permutation[j + 1], w_map)

    connect_places(permutation[count - 1], permutation[0], w_map)


def tabu_search(world_places):
    # TODO: Tabu Search
    from Tabu_Search import TabuSearch

    tabu_search_algo = TabuSearch(world_places, 50)
    final_permutation = tabu_search_algo.final_permutation

    return final_permutation


def simulated_annealing(world_places):
    # TODO: Simulated Annealing
    final_permutation = world_places
    return final_permutation


if __name__ == "__main__":
    amount = input("Amount of places 🏙️ >> ")
    while int(amount) < 5 or int(amount) > 240:
        print(f"‼️ Error ‼️\n\t- Minimal number of places is 5 and maximal is 240")
        amount = input("Amount of places 🏙️ >> ")

    world = World(amount)
    places = world.places
    print(f"\rGenerating world: loading 100% ✅", end="")
    sleep(.3)
    print("\r🌍 World has been successfully created with " + amount + " places 🏙️\n")

    root = Tk()
    root.attributes('-topmost', True)
    root.resizable(False, False)
    root.title("Travelling Salesman Problem 🚶‍♂️")

    world_map = Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    world_map.pack()

    i = 1
    for p in places:
        show_place(p, world_map, i)
        i += 1

    # print(f"distance between {places[0]} and {places[1]} is: {world.calculate_distance(places[0], places[1]):.2f}km")
    # connect_places(places[0], places[1], world_map)

    algo = int(
        input(
            "Choose algorithm for the Travelling Salesman Problem 🚶‍♂️\nTabu Search -> 1️⃣ | Simulated Annealing -> 2️⃣ >> ")
    )

    while algo != 1 and algo != 2:
        print("‼️ Error ‼️\n\t- Choose between 1️⃣ or 2️⃣")
        algo = int(
            input(
                "️Tabu Search -> 1️⃣ | Simulated Annealing -> 2️⃣ >> "
            )
        )

    best_permutation = []
    value = world.get_permutation_value(places)
    if algo == 1:
        best_permutation = tabu_search(places)
    elif algo == 2:
        best_permutation = simulated_annealing(places)

    print(f"\nOptimal trip length: {value:.2f}km 📏")
    root.title(f"Travelling Salesman Problem 🚶‍♂️- Optimal trip length: {value:.2f}km 📏")
    show_best_trip(best_permutation, world_map)

    print("\nℹ️ INFO: RESULT IS DISPLAYED IN WINDOW\n\t- Travelling Salesman Problem 🚶‍♂️")
    mainloop()
