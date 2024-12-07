washing_times = {
    "jacket": 40,
    "underwear": 70,
    "shoes": 20
}

program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ').strip().lower()
extra_rinse = input('Extra rinse? (y/n): ').strip().lower()
extra_spin = input('Extra spin? (y/n): ').strip().lower()

total_washing_time = 0

if program == "jacket":
    total_washing_time += washing_times["jacket"]
elif program == "u" or program == "underwear":
    total_washing_time += washing_times["underwear"]
elif program == "s" or program == "shoes":
    total_washing_time += washing_times["shoes"]
else:
    print("Invalid selection for washing program!")
    exit()  

if extra_rinse == "y":
    total_washing_time += 15

if extra_spin == "y":
    total_washing_time += 9

print(f"Total washing time: {total_washing_time} minutes")