files = input("File name: ")

if files.lower().endswith(".pdf"):
    print("application/pdf")
elif files.lower().endswith(".gif"):
    print("image/gif")
elif files.lower().endswith(".jpg"):
    print("image/jpeg")
elif files.lower().endswith(".png"):
    print("image/png")
elif files.lower().endswith(".txt"):
    print("text/plain")
elif files.lower().endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
