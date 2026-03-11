def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x_str, y_str = fraction.split("/")
            x = int((x_str))
            y = int((y_str))

            if y == 0 or x > y or x < 0 or y < 0:
                raise ValueError


            percent = percentage(x, y)
            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                 print(f"{percent:.0f}%")

            break

        except (ValueError, ZeroDivisionError):
            continue


def percentage(x, y):
    return (x / y) * 100



main()
