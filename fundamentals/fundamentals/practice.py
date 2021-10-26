# weekend = {
#     "Sunday": "church",
#     "Monday": "dim sum",
#     "Tuesday": "rehearsal",
#     "Wednesday": "teaching",
#     "Thursday": "gym",
#     "Friday": "swimming",
#     "Saturday": "concert"
# }

# print(weekend["Saturday"])

# food = {}
# food["breakfast"] = "eggs and home fries"
# food["lunch"] = "pasta"
# food["dinner"] = "kimchi fried rice"

# print(food)

# # del food["dinner"]
# print(food.keys())

# user = {
#     "first_name": "Melissa",
#     "last_name": "Cheng",
#     "age": 21,
#     "favorite_food": "potatoes"
# }

# if user["age"] > 21:
#     print("Access granted")
# elif user["age"] < 21:
#     print("You're too young")
# else:
#     print("Happy 21")

capitals = {
    "Washington":"Olympia",
    "California":"Sacramento",
    "Idaho":"Boise",
    "Illinois":"Springfield",
    "Texas":"Austin",
    "Oklahoma":"Oklahoma City",
    "Virginia":"Richmond"
}

# for key in capitals.keys():
#     print(key)

# for val in capitals.values():
#     print(val)

for key,val in capitals.items():
    print(key, " = ", val)