x = 7
y = 7

if x > y:
    print("Greater")
elif x < y:
    print("Less")
else:
    print("equal")


salary = int(input('What is your salary? '))

if salary >= 2000:
    print("You're eligible for mortgage")
    credit_score = int(input('What is your credit score? '))
    if 751 <= credit_score <= 800:
        print("Intereset percent is 6%")
    elif credit_score <= 750:
       print("Intereset percent is 8%")
    else:
        print("Intereset percent is 4%")
else:
    print("Sorry, you are not eligible")
