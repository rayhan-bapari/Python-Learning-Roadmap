greet = "Welcome to the trip cost calculator!"
print(greet)
days = input("How many days will you stay? ")
hotel_cost = input("How much does hotel cost per night? ")
flight_cost = input("How much does flight cost? ")
rental_cost = input("If you need rental car please enter the cost otherwise enter 0 ")
other_cost = input("Enter other possible expenses ")

total_hotel_cost = int(days) * int(hotel_cost)

total = round(total_hotel_cost + int(flight_cost) + int(rental_cost) + int(other_cost), 2)

print(f"Total costs: ${total}")
