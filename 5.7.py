import time

number_words = {5: "five", 4: "four", 3: "three", 2: "two", 1: "one"}

countdown = int(input("Enter the number of seconds to count down: "))


while countdown > 0:
    if countdown <= 5:  
        print(number_words[countdown])  
    else:
        print(countdown) 
    countdown -= 1
    time.sleep(1)

print("Time's up!")