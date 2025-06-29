def invest(amount, rate, years):
    for y in range(1, years + 1):
        amount *= 1 + rate
        print(f"year {y}: ${amount:.2f}")

a = float(input("Initial amount: "))
r = float(input("Annual rate (e.g. 0.05): "))
y = int(input("Years: "))
invest(a, r, y)
