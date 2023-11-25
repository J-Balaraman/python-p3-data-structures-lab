spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_names = []
    for n in range(len(spicy_foods)):
        for key in spicy_foods[n]: 
            spicy_names.append(spicy_foods[n][key]) if key == "name" else None
    return spicy_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
    return spiciest_foods


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: " + ("🌶" * heat_level))
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        if food["heat_level"] > 5:
            print(f"{name} ({cuisine}) | Heat Level: " + ("🌶" * heat_level))
    pass

def get_average_heat_level(spicy_foods):
    num_one = 0
    num_two = 0
    for food in spicy_foods:
        num_one += food["heat_level"]
        num_two += 1
    average = num_one / num_two
    return average

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_food_list = spicy_foods
    new_spicy_food_list.append(spicy_food)
    return new_spicy_food_list
