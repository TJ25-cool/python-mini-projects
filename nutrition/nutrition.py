fruits = {"apple": 130, "avocado": 50, "sweet cherries": 100, "kiwifruit" : 90, "pear": 100}


item = input("Item: ").lower().strip()
if item in fruits:
    print("Calories: ", fruits[item])
