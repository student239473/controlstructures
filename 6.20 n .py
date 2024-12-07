decimal_number = int(input("Enter decimal number: "))

remainders = []
while decimal_number > 0:
    remainder = decimal_number % 2  
    remainders.append(str(remainder))  
    decimal_number = decimal_number // 2  

binary_number = ''.join(remainders[::-1])

print(f"{decimal_number} (10) = {binary_number} (2)")