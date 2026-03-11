def convert(faces):
    faces = faces.replace(":)", "🙂")
    faces = faces.replace(":(", "🙁")
    return faces

def main():
    faces = input()
    result = convert(faces)

    print(result)

main()
