hours = input("Enter hours: ")
try:
    hour = float(hours)
except ValueError:
    print("Error, please enter numeric number input for hour")
    quit()

rate = input("Enter Rate: ")
try:
    rate = float(rate)
except ValueError:
    print("Error, please enter numeric number input for rate")
    quit()

if hour < 40:
    pay = round(hour * rate, 2)
else:
    overtime = hour - 40
    pay = round(40 * rate + overtime * rate * 1.5, 2)

output = f"Pay: {pay}"
print(output)
