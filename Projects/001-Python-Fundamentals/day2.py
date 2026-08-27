print("🐝 Welcome to BeeLabs Profile Builder 🐝")
while True:
    name = input("What is your name? ")
    try:
        if name: 
            break
        else:
            print("⚠️ Name cannot be empty.")
    except ValueError:
        print("⚠️ Please enter a valid name.")
while True:
    career = input("What career are you working toward? ")
    if career:
        break
    else:
        print("⚠️ Career cannot be empty.")

goal = input("What do you want to build? ")
while True:
    if goal:
        break
    else:
        print("⚠️ Goal cannot be empty.")
while True:
    try:
        years = int(input("How many years do you want to give yourself to reach your goal? "))
        if years > 0:
            break
        else:
            print("⚠️ Please enter a number greater than 0.")
    except ValueError:
        print("⚠️ Please enter a number, like 2.")
while True:
    language = input("What programming language are you learning? ")
    if language:
        break
    else:
        print("⚠️ Language cannot be empty.")
print()
print("----- YOUR BEELABS PROFILE -----")
print("Name:", name)
print("Career Goal:", career)
print("I want to build:", goal)
print("Timeline:", years, "years")
print("Programming language:", language)
print("--------------------------------")

if years <= 2:
    print("That is an aggressive goal. Time to build!")
elif years <= 3:
    print("Great timeline! Stay consistent and keep building!")
else:
    print("You have time, but consistency still matters.")

if language.lower()== "python":
    print("🐍 Great choice! Python is perfect for building AI and automation.")

elif language.lower() == "javascript":
    print("🌐 Nice! JavaScript is powerful for building interactive websites.")

else:
    print("That's a good language too! Keep learning and building!")   
