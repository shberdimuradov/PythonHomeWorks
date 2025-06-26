def check_password():
    password = input("Parol kiriting: ")

    if len(password) < 8:
        print("Parol juda qisqa.")
    elif not any(char.isupper() for char in password):
        print("Parolda kamida bitta katta harf bo‘lishi kerak.")
    else:
        print("Parol mustahkam.")

check_password()
