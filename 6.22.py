for num in range(1, 31):
    if num % 3 == 0 and num % 5 == 0:
        print("BINGO", end=" ")
    elif num % 3 == 0:
        print("THREE", end=" ")
    elif num % 5 == 0:
        print("FIVE", end=" ")
    else:
        print(num, end=" ")