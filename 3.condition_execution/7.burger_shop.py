greet = "Burger Shop"

size = input("What size burger do you want? M, N or L ").capitalize()
add_mashroom = input("Do you want to add Mashroom? Y or N ").capitalize()
extra_chesse = input("Do you want to add extra cheese? Y or N ").capitalize()

bill = 0

if size == "M":
    bill += 5
elif size == "N":
    bill += 8
else:
    bill += 10

if add_mashroom == "Y":
    if size == "M":
        bill += 1
    elif size == "N":
        bill += 1
    else:
        bill += 2

if extra_chesse == "Y":
    if size == "M":
        bill += 1
    elif size == "N":
        bill += 1
    else:
        bill += 1

total = f"Your total bill is: {bill}"
print(total)
