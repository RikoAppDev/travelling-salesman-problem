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


def tabu_search(w, max_iter):
    from TabuSearch import TabuSearch

    tabu_search_algo = TabuSearch(w, max_iter, 50)
    final_permutation = tabu_search_algo.final_permutation

    return final_permutation


def simulated_annealing(world_places):
    # TODO: Simulated Annealing
    final_permutation = world_places
    return final_permutation


if __name__ == "__main__":
    amount = input("Amount of places 🏙️ >> ")
    while int(amount) < 3 or int(amount) > 240:
        print(f"‼️ Error ‼️\n\t- Minimal number of places is 3 and maximal is 240")
        amount = input("Amount of places 🏙️ >> ")

    world = World(amount)
    places = world.places
    sleep(.3)
    print("\r🌍 World has been successfully created with " + amount + " places 🏙️\n")

    root = Tk()
    root.attributes('-topmost', True)
    root.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT, root.winfo_screenwidth() - WINDOW_WIDTH - 10, 0))
    root.resizable(False, False)
    root.title("Travelling Salesman Problem 🚶‍♂️")

    world_map = Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    world_map.pack()

    i = 1
    for p in places:
        show_place(p, world_map, i)
        i += 1

    algo = int(
        input(
            "Choose algorithm for Travelling Salesman Problem 🚶‍♂️\nTabu Search -> 1️⃣ | Simulated Annealing -> 2️⃣ >> "
        )
    )
    while algo != 1 and algo != 2:
        print("‼️ Error ‼️\n\t- Choose between 1️⃣ or 2️⃣")
        algo = int(
            input(
                "️Tabu Search -> 1️⃣ | Simulated Annealing -> 2️⃣ >> "
            )
        )

    iterations = int(input("Number of iterations ♻️ (optimal 500) >> "))
    while iterations < 1:
        print("‼️ Error ‼️\n\t- Input positive not null number")
        iterations = int(input("Number of iterations ♻️ (optimal 500) >> "))
    print()

    best_permutation = []
    if algo == 1:
        best_permutation = tabu_search(world, iterations)
    elif algo == 2:
        best_permutation = simulated_annealing(places)

    value = world.get_permutation_value(best_permutation)

    print(f"\n\nOptimal trip length: {value:.2f}km 📏")
    root.title(f"Travelling Salesman Problem 🚶‍♂️- Optimal trip length: {value:.2f}km 📏")
    show_best_trip(best_permutation, world_map)

    print("\nℹ️ INFO: RESULT IS DISPLAYED IN WINDOW\n\t- Travelling Salesman Problem 🚶‍♂️")
    mainloop()
