print("🐝 Welcome to BeeLabs Profile Builder 🐝")

name = input("What is your name? ")
career = input("What career are you working toward? ")
goal = input("What do you want to build? ")
years = int(input("How many years do you want to give yourself to reach your goal? "))
language = input("What progamming language are you learning?" )

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


