total_sum = 0
count = 0  # To keep track of the number of inputs

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  
    total_sum += number
    count += 1 

if count > 0:  
    mean = total_sum / count
    print(f"The total sum of the numbers is: {total_sum}")
    print(f"The arithmetic mean of the numbers is: {mean}")
else:
    print("No numbers were entered.")