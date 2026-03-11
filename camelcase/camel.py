snakes = [{"camelCase": "name", "snake_case": "name"},
           {"camelCase": "firstName", "snake_case": "first_name"},
           {"camelCase": "preferredFirstName", "snake_case": "preferred_first_name"}
           ]

camels = input("camel_Case: ")

for c in snakes:
    if c["camelCase"] == camels:
        print(c["snake_case"])
