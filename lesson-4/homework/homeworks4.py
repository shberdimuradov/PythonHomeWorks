import random

def play_game():
    number = random.randint(1, 100)
    attempts = 10

    print("1 dan 100 gacha bo‘lgan raqamni toping. Sizda 10 urinish bor!")

    for i in range(attempts):
        try:
            guess = int(input(f"{i+1}-urinish: "))
        except ValueError:
            print("Iltimos, butun son kiriting.")
            continue

        if guess < number:
            print("Juda kichik!")
        elif guess > number:
            print("Juda katta!")
        else:
            print("To\'g\'ri topdingiz!")
            return  # o‘yin tugadi

    print("Yutqazdingiz. Yana o‘ynashni xohlaysizmi?")

def main():
    while True:
        play_game()
        replay = input(">> ").strip().lower()
        if replay not in ['y', 'yes', 'ok']:
            print("O‘yin tugadi.")
            break

if __name__ == "__main__":
    main()