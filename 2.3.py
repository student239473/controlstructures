driving_mode = input('Enter driving mode (A/M/E): ')
distance = int(input('Enter distance in km: '))

if driving_mode == 'A':
    fuel_consumption = 7  
elif driving_mode == 'M':
    fuel_consumption = 9  
elif driving_mode == 'E':
    fuel_consumption = 6  
else:
    fuel_consumption = 0  

if fuel_consumption > 0:
    total_consumption = (fuel_consumption / 100) * distance
    print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption:.2f} liters')
else:
    print('Invalid driving mode entered.')