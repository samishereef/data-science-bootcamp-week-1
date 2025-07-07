'''cities = ["paris", "milan","kuwait", "miami", "atlanta"]
cities[1]= "Boston"
print(cities)'''


'''animals = ["Dog", "Cat", "Rabbit", "Hamster"]
del animals[0]
print(animals)'''


'''students = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]
students[3] = "Diane"
students.append("Grace")
students.insert(3, "Henry")
students.remove("Bob")
last_student = students.pop()
print(last_student)
del students[1]
print(students)'''

'''colors=["red","blue","green","pink","Orange"]
print(colors[0:3])'''

'''numbers=[1,2,3,4,5]
numbers.reverse()
print(numbers)'''


'''colors=["red","blue","green","yellow"]
print(len(colors))'''



'''numbers=[10,20,30,40,50]
print(numbers)'''

'''numbers=[10,20,30,40,50]
numbers.insert(2, 25)
print(numbers)'''


'''numbers=[10,20,30,40,50]
numbers.remove(40)
print(numbers)'''




'''numbers=[10,20,30,40,50]
last_num=numbers.pop()
print(last_num)
print(numbers)'''



'''numbers = [1,2,3,4,5]
second_number=numbers.pop(1)
print(second_number)'''






'''animals=["cat","dog","mouse"]
animals.append("Rabbit")
animals.insert(1, "Hamster")
animals[2]="Puppy"
animals.remove("mouse")
last_animal=animals.pop()
del animals[0]
print(animals)'''





'''numbers = [5,2,9,1,4]
numbers.sort(reverse=True)
print(numbers)'''





'''colors1=["red", "blue"]
colors2 = ["green", "yellow"]
colors1.extend(colors2)
print(colors1)'''






'''numbers = [10,20,30,40,50]
print(numbers)'''






'''numbers = [10,20,30,40,50]
numbers.insert(2, 25)
print(numbers)'''





'''numbers = [10,20,30,40,50]
numbers.insert(2, 25)
numbers.remove(40)
print(numbers)'''





'''numbers = [10,20,30,40,50]
numbers.insert(2, 25)
numbers.remove(40)
last_num=numbers.pop()
print(last_num)
print(numbers)'''






'''numbers = [10,20,30,40,50]
numbers.insert(2, 25)
numbers.remove(40)
last_num=numbers.pop()
del numbers[0]
print(numbers)'''





'''colors = ["red", "blue", "green", "yellow"]
second_num=colors.pop(1)
print(second_num)
print(colors)'''






'''fruits=["apple","bannana"]
fruits2=["cherry","orange"]
fruits.extend(fruits2)
print(fruits)'''








'''numbers=[8,3,1,6,5]
numbers.sort(reverse=True)
print(numbers)'''





'''fav_movies =["god","mom","dad","sis","bro"]
print(fav_movies[0:3])'''






'''car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020
}
print(car)'''


'''car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020
}
print(car["model"])'''






'''car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020
}
car["color"]= "red"
print(car)'''






'''book = {
    "title": "gatsby",
    "author": "George Orwell",
    "year": 1949
}
print(book)'''




'''book = {
    "title": "gatsby",
    "author": "George Orwell",
    "year": 1949
}
print(book["author"])'''





'''book = {
    "title": "gatsby",
    "author": "George Orwell",
    "year": 1949
}
book["genre"] = "Dystopian"
print(book)'''





'''book = {
    "title": "gatsby",
    "author": "George Orwell",
    "year": 1949
}
print(book)'''





'''movie = {
    "title":"Inception",
    "director": "Christopher Nolan",
    "year": 2010
}
movie["Genre"]="Science Fiction"
moive_genre=movie.pop("Genre")
print(movie)'''






'''student= {
    "name": "John Doe",
    "age": 21,
    "major": "biology"
}
student["GPA"] = 3.5
student["major"] = "Chemistry"
student_gpa=student.pop("GPA")

print(student)'''





'''employee = {
    "name": "Sarah",
    "department": "Sales",
    "details": {
        "email": "sarah@sales.com",
        "phone": "555-0000"
    }
}
employee["details"]="office":"Downtown"
print(employee["details"]["phone"])'''




'''course = {
    "title": "Data Science 101",
    "instructor": "Dr. Smith",
    "schedule": {
        "day": "monday",
        "time": "10:00 AM"

    }
}
course["schedule"]["room"]="A101"
print(course)'''





'''pet = {
    "type":"dog",
    "name":"Buddy",
    "age": 5
}
for key in pet:
    if key == "name":
        print(pet[key])'''






'''recipe = {
    "name": "pancakes",
    "servings": 4,
    "time": "20 minutes"
    }
for key in recipe:
    if key == "time":
        print(recipe[key]) '''




'''city_info = {
    "name": "Paris",
    "country": "France",
    "population": "2 million"
}
for key in city_info:
    if key == "country":
        print(city_info[key])'''






'''colors = {"red", "green", "blue"}
if "red" in colors:
    print(colors)'''



'''animals = {"cat", "dog", "rabbit"}
animals.add("Hamster")
animals.remove("cat")
animals.empty()
print("rabbit" in animals)'''


'''set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print'''



'''numbers = {10, 20, 30}
numbers.add(40)
numbers.remove(20)
more_numbers = {30,40,50,60}
print(numbers.symmetric_difference(more_numbers))'''


'''fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.remove("banana")
fruits.insert(1, "kiwi")
print(fruits)'''


'''car = {
    "brand":"toyota",
    "model":"Corolla",
    "year":2020
}
car["color"]=["blue"]
for value in car.values():
    if value == "brand":
        print(car)'''





'''animals = ["cat", "dog", "rabbit"]
animals.append("hamster")
last_animal = animals.pop()
animals.insert(1, "turtle")
print(last_animal)
print(animals)'''



'''book = {
    "title": "Gatsby",
    "author": "George Orwell",
    "year": 1949
}
book["year"] = 1950
for key, value in book.items(): 
print(book)'''




'''cities = ["New York", "Paris", "Tokyo"]
cities.append("london")
cities.remove("Paris")
cities.insert(2, "Berlin")
print(cities)'''





'''movie = {
    "title": "inception",
    "director": "Christopher Nolan",
    "year": 2010
}
movie["Genre"] = "Science Fiction"
for key, value in movie.items():
    print(key, value)'''



'''vehicles = {"Car", "bike", "bus"}
vehicles.add("train")
print("Car" in vehicles)'''


'''numbers = [5, 10, 15, 20, 25]
numbers.insert(2, 12)
numbers[:3]
print(numbers.pop())'''



'''student = {
    "name": "Alice",
    "age": 22,
    "major": "Math"
}
student["GPA"] = "3.8"
for key, value in student.items():
    print(f"{key}: {value}")'''



'''set_a= {1,2,3}
set_b={3,4,5}
print(set_a.difference(set_b))'''








