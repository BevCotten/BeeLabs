print("🐝 Welcome to the BeeLabs Career Matcher!")

name = input("What is your name? ")
favorite_activity = input(
    "Which sounds most exciting: building, analyzing, or designing? "
).strip().lower()

print(f"\nOkay, {name}! Let's explore your tech path.")

if "designing" in favorite_activity and "analyzing" in favorite_activity:
    print("You may enjoy AI Product Engineering!")
elif "building" in favorite_activity and "analyzing" in favorite_activity:
    print("You may enjoy Machine Learning Engineering!")
elif "building" in favorite_activity and "designing" in favorite_activity:  
    print ("You may enjoy Full Stack Development!")
elif "building" in favorite_activity:
    print("You may enjoy Software Engineering!")
elif "analyzing" in favorite_activity:
    print("You may enjoy Data Science or Artificial Intelligence!")
elif "designing" in favorite_activity:
    print("You may enjoy Front-End Development or UX Engineering!")
else:
    print("That wasn't one of the choices—but tech has plenty of other paths!")