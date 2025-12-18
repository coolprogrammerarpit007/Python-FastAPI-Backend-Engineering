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

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

index = 0

while(index < 3):
    for day in my_list:
        if day == "Monday":
            continue
        
        print(f"WeekDay: {day}")
    print(f"************ WeekDays ***********")
    index += 1