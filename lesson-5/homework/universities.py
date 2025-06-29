universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(data):
    s = [row[1] for row in data]
    t = [row[2] for row in data]
    return s, t

def mean(lst): return sum(lst) / len(lst)
def median(lst):
    lst = sorted(lst)
    l = len(lst)
    return (lst[l//2] if l % 2 else (lst[l//2 - 1] + lst[l//2]) / 2)

students, tuitions = enrollment_stats(universities)
print("*" * 30)
print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(tuitions):,}")
print()
print(f"Student mean: {mean(students):,.2f}")
print(f"Student median: {int(median(students))}")
print()
print(f"Tuition mean: $ {mean(tuitions):,.2f}")
print(f"Tuition median: $ {int(median(tuitions))}")
print("*" * 30)
