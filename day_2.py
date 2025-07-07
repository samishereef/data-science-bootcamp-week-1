''' age = int(input("enter your age: "))
if age > 21:
    print("access granted.")
else:
    print("access denied. you must be at least 21.") '''

'''age = int(input("Enter your age: "))
if age < 5:
    print("ticket is free.")
elif age >=5  and age <=12:
    print("ticket is $5")
elif age >=13 and age <=59:
    print("ticket is $12")
elif age >=60:
    print("ticket is $7") '''


''' age = int(input("Enter your age: "))
if 16 <= age <=17:
    permission = input("Do you have a parent or guardian's permission? (yes/no): ")
    if permission == "yes":
        print("you are allowed to join.")
    else:
        print("you are not allowed to join.")
elif age <16:
    print("you are not allowed to join")
elif age >=18:
    print("you automatically qualify.")
elif age >= 60:
    print("You are eligible for a senior discount.")
else:
    print("You automatically qualify.") '''

''' cart_total = float(input("enter the total amount of your cart: "))
customer = input("are you a student? (yes/no): ")
if customer == "yes" and {cart_total >= 50}:
    discount = cart_total * 0.15
    total_amount = cart_total - discount
    print(f"you get a 15% discount. your total amount is: ${total_amount:.2f}")
if customer == "no" and cart_total >= 100:
    discount = cart_total * 0.10
    total_amount = cart_total - discount
    print(f" you get a 10% discount. your total amount is: ${total_amount:.2f}")
if customer == cart_total < 20:
    print(f"no discount applicable. your total amount is: ${cart_total:.2f}")
elif (customer == "yes" or customer == "no") and cart_total >= 20 or cart_total <= 50:
    discount = cart_total * 0.05
    total_amount = cart_total - discount
    print(f"you get a 5% discount. your total amount is: ${total_amount:.2f}") '''



'''diet = input("what is your diet? (vegetairan/keto/regular)").lower()
time_of_day = input("what time of day is it? (breakfast/lunch/dinner)").lower()'''

''' if diet == "vegetarian":
  print("a salad")
elif diet == "keto":
  print("a keto bowl")
elif diet == "regular":
  print("a regular meal")
else:
    print("a default meal")

if time_of_day == "breakfast":
    print("early bird gets the worm")
elif time_of_day == "lunch":
    print("lunch is served")
elif time_of_day == "dinner":
    print("dinner is ready") '''


'''room = input("Which room are you in? (kitchen/bedroom/living room): ").lower()
time_of_day = input("What time of day is it? (morning/afternoon/night): ").lower()

if room == "kitchen":
    print("How about making a coffee?")
elif room == "bedroom":
    print("WOuld you like to rest?")
elif room == "living room":
    print("Maybe turn on the TV")

if time_of_day == "morning":
    print("Good morning! Have a great start to your day!")
elif time_of_day == "afternoon":
    print("Good afternoon! Hope you're having a productive day!")
elif time_of_day == "night":
    print("Good night! Time to relax and unwind!")'''

'''room = input("Which room are you in? (kitchen/bedroom/living room): ").lower()
time_of_day = input(" What time of day is it? (morning/afternoon/night): ").lower()

if room == "kitchen":
    print("How about making a coffee?")
elif room == "bedroom":
    print("Would you like to rest?")
elif room == "living room":
    print("Maybe turn on the TV")  
else: 
    print("I'm not sure what to suggest for that room.")

if time_of_day == "morning":
    print("Good morning! Have a great start to your day!")
elif time_of_day == "afternoon":
    print("Good afternoon! Hope you're having a productive day!")
elif time_of_day == "night":
    print("Good night! Time to relax and unwind!")

if room == "kitchen" and time_of_day == "morning":
    print("You could start breakfast now")
elif room == "bedroom" and time_of_day == "night":
    print("It's a good time to sleep")
elif room == "living room" and time_of_day == "afternoon":
    print("You could watch a movie or read a book")
else:
    print("Enjoy your time in the room!")'''

'''weather = input("What is the weather like where you're going? (hot/cold/mild): ").lower()
days = int(input("How many days will you be traveling?"))
packed = input("have you already packed? (yes/no): ").lower()


if weather == "hot":
    print("pack shorts and sunscreen.")
elif weather == "cold":
    print("pack a jacket and gloves.")
elif weather == "mild":
    print("pack light layers.")
else:
    print("check the forecast before you go.")
if days >= 5:
    print("Don't forget extra socks and underwear!")
if packed == "no" and days > 3:
    print("You should start packing soon!")'''






'''age = int(input("Enter your age: "))
if age < 16:
    print("You are not eligible to drive.")
drivers_license = input("Do you have a driver's license? (yes/no): ").lower()
if drivers_license == "yes":
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.") 
time = input("What time of day is it? (morning/afternoon/night)").lower()

if 16 <= age <= 19 and time == "night":
    print("You need to be home by 10 PM.")
elif 20 <= age <= 25 and time == "night":
    print("You need to be home by 11 PM.")
elif age > 25 and time == "night":
    print("You can stay out as late as you want.")'''





''' age = int(input("Enter your age: "))
student_ID = input("Do you have a student ID? (yes/no): ").lower()
day = input("What day of the week is it? (Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday): ").lower()
time = input("What time of day is it? (morning/afternoon/evening): ").lower() '''


''' if age < 12:
    print("You are not eligible for a student discount.")
elif 12 <= age <= 25 and student_ID == "yes":
    print("You are eligible for a %25 discount.")
elif day == ("saturday" or "sunday") and time == "evening":
    print("Weekend special: Free Drink included!")
elif age >= 60:
    print("You are eligible for a %10 senior discount.")
else:
    print("Standard rate applies.") '''





'''age = int(input("Enter your age: "))
student = input("Are you a student? (yes/no): ").lower()
day = input("What day of the week is it? (Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday) ").lower()
time = input("What time is your movie (Matinee/evening): ").lower()

if age < 13:
    print("The ticket is $8")
elif 13 <= age <= 60:
    print("The ticket price is $12")
else:
    print("The ticket price is $7")

if student == "yes" and (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day) and time == "Matinee":
    print("The Price of your ticket is $6")
elif day == "Friday" and time == "evening":
    print("The Price of your ticket is $15")'''








'''age = int(input("What is your age: "))
student = input("Are you a student (yes/no)?").lower()
time= input("Morning/Afternoon/Evening: ").lower()
day= input("What Day of the week is it? (Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday:)").lower()

membership = 100
final_price = 0

if student == "yes" and day in ["monday", "tuesday", "wednesday", "thursday", "friday"] and time == "morning":
    final_price = membership - (membership * .25)


if age <= 18:
    final_price = 20
elif age >= 60:
    final_price = membership - (membership * .30)

if day == "saturday" or "sunday" and time == "evening":
   final_price = final_price + 10

print(f"Your final gym membership fee is: {final_price} ")'''







age = int(input("How old are you?"))
day_late = int(input("How many days late is your book?"))
member = input("Are you a Member? (yes/no):")
Day = input("What day of the week is it? (monday,tuesday, wednesday, thursday, friday, saturday, sunday)? ")

fee = 1.50 * day_late

if age < 12:
    fee = 0
elif age >=65:
    fee = fee *.50

if Day == "sunday":
    fee = fee + 2

print(f" Your total late fee is: {fee}")




    