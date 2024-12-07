hours_parked = int(input("Enter the number of hours parked: "))

if 1 <= hours_parked <= 2:
    fee = 5
elif 3 <= hours_parked <= 6:
    fee = 15
elif hours_parked > 6:
    fee = 20
else:
    fee = 0  # For invalid inputs like 0 or negative hours

if hours_parked > 0:
    print(f"The parking fee is: {fee} PLN")
else:
    print("Invalid number of hours entered.")