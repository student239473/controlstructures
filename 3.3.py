age = int(input('Enter your age: '))

if age < 18 or age >= 65:
    print(f'Age {age}: Eligible for discount')
else:
    print(f'Age {age}: Not eligible for discount')