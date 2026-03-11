def main ():
    plate  = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if  not s.isalnum():
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    first_number = 1
    for i in range(len(s)):
        if s[i].isdigit():
            first_number = i
            break

    if first_number == 1:
        return True
    if s[first_number] == "0":
        return False

    for _ in range(first_number, len(s)):
        if s[_].isalpha():
            return False
    return True





main()
