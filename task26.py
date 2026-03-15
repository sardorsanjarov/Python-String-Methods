username = input("Username kiriting: ")

check = username.replace("-", "")

if check.isalpha():
    print(True)
else:
    print(False)