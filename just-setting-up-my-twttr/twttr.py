vowels = ["A", "a","e", "i", "E", "I", "O", "o", "u", "U"]



def letter(user_input):
    output = ' '
    for letter in user_input:
         if letter not in vowels:
               output += letter
    return output



def main():
     user_input = input("Input: ")
     output = letter(user_input)
     print(f"Output: {output}")






main()
