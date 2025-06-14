x = 5
y = 7

if x == y:
    print("Equal")
else:
    if x > y:
        print("Less")
    else:
        print("greater")

salary = int(input('What is your salary? '))

if salary >= 2000:
    print("You're eligible for mortgage")
    credit_score = int(input('What is your credit score? '))
    if credit_score <= 800:
        print("Intereset percent is 6%")
    else:
        print("Intereset percent is 4%")
else:
    print("Sorry, you are not eligible")
