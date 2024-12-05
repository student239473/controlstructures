university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded = university_expanded + char + ' '

print(university)  # Original university name
print(university_expanded.strip())  # Expanded university name