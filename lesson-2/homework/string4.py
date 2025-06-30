first_palindrom = 'madam'
second_palindrom = 'racecar'
num_polindrom = '12321'

if first_palindrom[0:5] == first_palindrom[::-1] and second_palindrom[0:7]==second_palindrom[::-1] and num_polindrom[0:5]==num_polindrom[::-1]:
    print('polindrom') 
else:
    print('No polindrom')