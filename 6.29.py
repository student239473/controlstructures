def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


N = int(input("Enter the number of prime numbers to find: "))


primes = []

number = 2  
while len(primes) < N:
    if is_prime(number):
        primes.append(number)
    number += 1

print("Prime numbers:", ' '.join(map(str, primes)))