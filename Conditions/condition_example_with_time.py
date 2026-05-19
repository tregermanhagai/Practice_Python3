from datetime import datetime

print("Current time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

now = datetime.now()

hour = now.hour

print("The hour now is: ", hour)
print(f"The hour now is: {hour}")

if hour >=12 and hour < 16:
    print("Good midday")
elif hour >= 16 and hour < 18:
    print("good afternoon")
elif hour >= 18:
    print("good evning")
else:
    print("No matching")


if hour != 20:
    print("hour is 20")
else: print("Not 20")