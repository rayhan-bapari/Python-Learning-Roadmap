greet = "Burger Shop"

size = input("What size burger do you want? M, N or L ").capitalize()
add_mashroom = input("Do you want to add Mashroom? Y or N ").capitalize()
extra_chesse = input("Do you want to add extra cheese? Y or N ").capitalize()

bill = 0

if size == "M" and add_mashroom == "Y" and extra_chesse == "Y":
    bill += 5 + 1 + 1
elif size == "M" and add_mashroom == "Y" and extra_chesse == "N":
    bill += 5 + 1
elif size == "M" and add_mashroom == "N" and extra_chesse == "N":
    bill += 5
elif size == "N" and add_mashroom == "Y" and extra_chesse == "Y":
    bill += 8 + 1 + 1
elif size == "N" and add_mashroom == "Y" and extra_chesse == "N":
    bill += 8 + 1
elif size == "N" and add_mashroom == "N" and extra_chesse == "N":
    bill += 8
elif size == "L" and add_mashroom == "Y" and extra_chesse == "Y":
    bill += 10 + 2 + 1
elif size == "L" and add_mashroom == "Y" and extra_chesse == "N":
    bill += 10 + 2
else:
    bill += 10

total = f"Your total bill is: {bill}"
print(total)
