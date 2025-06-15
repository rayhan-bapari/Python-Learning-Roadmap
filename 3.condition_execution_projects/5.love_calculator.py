greet = "Welcome to love calculator"
print(greet)

your_name = input("Enter your name: ")
lover_name = input("Enter your lover name: ")

combined_name = your_name + lover_name
lower_name = combined_name.lower()

true = (
    lower_name.count("t")
    + lower_name.count("r")
    + lower_name.count("u")
    + lower_name.count("e")
)


love = (
    lower_name.count("l")
    + lower_name.count("o")
    + lower_name.count("v")
    + lower_name.count("e")
)

score = int(str(true) + str(love))

if score < 10 and score > 85:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 70:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")
