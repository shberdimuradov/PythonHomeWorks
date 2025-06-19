# 3st.
number = int(input('Please enter your number: '))

if number == 0:
    print("0 — bu juft son")
elif number > 0 and number % 2 == 0:
    print("Musbat juft son")
elif number > 0 and number % 2 != 0:
    print("Musbat toq son")
elif number < 0 and number % 2 == 0:
    print("Manfiy juft son")
else:
    print("Manfiy toq son")
