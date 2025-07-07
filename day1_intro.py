'''
Challenge: Annual Sports Gala Budget
You are managing the budget for a city's Annual Sports Gala.
Here are the known costs and revenue details:

🎟️ Expenses:
Venue rental: 120,000 KWD
Lighting & Sound: 65,000 KWD
Guest performances: 90,000 KWD
Decorations & branding: 30,000 KWD
💰 Ticket Info:
Tickets sold: 950
Ticket price: 350 KWD per ticket
🎯 Your Task:
Using hardcoded variables (no input() this time):

Calculate the total cost of the event
Calculate the total revenue
Calculate the profit or loss
Calculate the cost per attendee
Print all values formatted to two decimal places and labeled with KWD
✅ Sample Output:
Total event cost: 305000.00 KWD  
Total ticket revenue: 332500.00 KWD  
Profit: 27500.00 KWD  
Cost per attendee: 321.05 KWD
You’re free to format your print statements how you like — as long as the math is accurate and the output is readable.
'''


venue_rental = int(input("Enter the rental fee for the venue: "))
name = input('what is your name')


number1  = 123
number2 = '456'
age = input('what is your age:')
nextYearAge = age + 1

w = int('123')


lighting_cost = int(input("Enter the cost of lighting: ")) #this is info for me 
entertainment = int(input("Enter the cost of entertainment: "))
decorations = int(input("Enter the cost of decorations: "))
tickets = int(input("Enter the number of tickets sold: "))
ticket_price = int(input("Enter the price of each ticket: "))
total_cost = venue_rental + lighting_cost + entertainment + decorations
total_revenue = tickets * ticket_price
profit = total_revenue - total_cost
cost_per_person = total_cost / tickets if tickets > 0 else 0
print(f"Total cost: ${total_cost:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")
print(f"Profit: ${profit:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")

'''cost = int(input("Enter the cost of the event: "))
revenue = int(input("Enter the revenue from ticket sales: "))
profit = revenue - cost
print(f"Total profit: {profit:.2f} KWD") '''



'''age = int(input("Enter your age: ")) *7
print(f"Your age in dog years is: {age}")'''


'''net_worth = int(input("Enter your net worth: "))
cost_of_meal = int(input("Enter the cost of your meal: "))
if cost_of_meal > net_worth:
    print("You can't afford this meal.")
else:
    print("You can afford this meal.") '''


'''minutes_worked = int(input("Enter the number of minutes worked: "))
minutes_per_hour = 60
hours_worked = minutes_worked / minutes_per_hour
print(f"You have worked for {hours_worked:.2f} hours.")'''











name = input("Enter your name: ")
monthly_salary = int(input("Enter your monthly salary: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
money_left = monthly_salary - monthly_expenses
print(f" Hello {name}, you have {money_left} KWD left after all your expenses this month.")




