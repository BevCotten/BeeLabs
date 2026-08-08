print ("BeeLabs Day 3")
for number in range (10, 0, -1):
    print(number) 
for number in range (1,11):
    if number == 5:
        print("5 - Halfway there!")
    else: 
        print(number)
print("BeeLabs launched!")
for number in range (1,21):
    if number == 10:
        print("10 - BeeLabs is halway!") 
    else:
        print(number)
print("Day 3 completed")
projects = ["Website", "Calculator", "AI Assistant"] 

for project in projects: 
    print(project)  
new_project = input("What project should BeeLabs build next? ")

projects.append(new_project)

print("Updated BeeLabs project list:")

for project in projects:
    print(project)  
def welcome(name):
    print(f"Welcome to BeeLabs, {name}!")
    print("Let's build something amazing") 
welcome("Beverly")    
welcome("Bee")   
welcome("Bee")
welcome("Developer")