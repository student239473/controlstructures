time_24hr = input("Enter time (24-hour format): ")

hours, minutes = map(int, time_24hr.split(":"))

if hours == 0:
    hours_12hr = 12
    am_pm = "am"
elif hours > 12:
    hours_12hr = hours - 12
    am_pm = "pm"
elif hours == 12:
    hours_12hr = 12
    am_pm = "pm"
else:
    hours_12hr = hours
    am_pm = "am"

time_12hr = f"{hours_12hr}:{minutes:02d}{am_pm}"

print("Time in 12-hour format:", time_12hr)