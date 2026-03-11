def due():
    amount = 50
    coins = [25, 10, 5]


    while amount > 0:
        print("Amount Due: " + str(amount))
        coin = int(input("Insert Coin: "))
        if coin in coins:
            amount -= coin
    return abs(amount)


def main():
    change = due()
    print("Change Owed: ", change)


main()
