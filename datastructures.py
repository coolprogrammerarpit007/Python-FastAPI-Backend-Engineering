zoo_animals = ['lion','tiger','elephant','bear','monkey']
# print(zoo_animals)

removed_animal = zoo_animals.pop(3)
# print(zoo_animals)

zoo_animals.append("Zebra")
# print(zoo_animals)
# print(zoo_animals[0:3])




# grade = int(input("Enter your marks: "))


# if(grade >= 90 and grade <= 100):
#     print("Grade A")
    
# elif(grade >= 80 and grade <= 89):
#     print("Grade B")
    
# elif(grade >= 70 and grade <= 79):
#     print("Grade C")
    
# elif(grade >= 60 and grade <= 69):
#     print("Grade D")
    
# else:
#     print("Grade: F")
    


# Loops Assignment 

# my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# index = 0

# while(index < 3):
#     for day in my_list:
#         if day == "Monday":
#             continue
        
#         print(f"WeekDay: {day}")
#     print(f"************ WeekDays ***********")
#     index += 1



#  dictionary assignment

my_vehicle = {
    "model":"Ford",
    "make":"Explorer",
    "year":2018,
    "mileage":40000
}

# for key,value in my_vehicle.items():
#     print(f"Vehicle {key}: {value}")
    
vehicle2 = my_vehicle.copy()
vehicle2["number_of_tires"] = 4
del vehicle2["mileage"]
# print(vehicle2)
# print(vehicle2.keys())

# function assignments

def person_info(firstname,lastname,age):
    return {
        "user_first_name":firstname,
        "user_last_name":lastname,
        "age":age
    }
    
person_details = person_info(lastname="Mishra",firstname="Arpit",age=25)
print(person_details)