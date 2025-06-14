greet = "Body Mass Index (BMI) Calculator"
print(greet)

weight = float(input("What is your weight? "))
height = float(input("write your height in meter? "))

bmi = round(weight / height**2, 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are normal range")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight")
else:
    print(f"Your bmi is {bmi}, you are obese")
