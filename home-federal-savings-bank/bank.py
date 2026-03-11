greeting = input("Greeting: ")

if greeting == "Hello" or greeting == "Hello, Newman":
    print("$0")
elif greeting == "How you doing?" or greeting.startswith("H"):
    print("$20")
else:
    print("$100")
