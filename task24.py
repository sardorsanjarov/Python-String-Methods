email = input("Email kiriting: ")

if not email.startswith("@") and email.endswith(".com"):
    print(True)
else:
    print(False)