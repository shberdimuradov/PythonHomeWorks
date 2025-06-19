num1 = float(input('Please enter first number: '))
num2 = float(input('Please enter second number: '))
num3 = float(input('Please enter third number: '))

if num1 != num2 and num1!=num3 and num2!=num3:
    print('Numbers are not equal')
elif  num1 == num2 and num1==num3 and num2==num3: 
    print('Numbers are equal') 
else:
    print('Some numbers are equal')