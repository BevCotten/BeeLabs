import random
print("✨ Welcome to Bee's Virtual Stylist ✨")

name = input("Client's name: ")
occasion = input("Where are you going—work, date, or brunch? ").strip().lower()
weather = input("Is it hot or cold? ").strip().lower()

print(f"\nStyling {name}...")

if occasion == "work" and weather == "hot":
    outfit = "a satin blouse, wide-leg trousers, and brown horsebit loafers"
elif occasion == "work" and weather == "cold":
    outfit = "a fitted turtleneck, tailored trousers, and ankle boots"
elif occasion == "date" and weather == "hot":
    outfit = "a satin midi dress, strappy heels, and gold accessories"
elif occasion == "date" and weather == "cold":
    outfit = "a fitted sweater dress, tall boots, and a chic coat"
elif occasion == "brunch":
    outfit = "a flowy dress, stylish sandals, and a structured tote"
else:
    outfit = "a polished matching set with your favorite accessories"
accessories = [
    "gold hoop earrings",
    "a nice clutch bag",
    "a nice designer belt",
    "a nice manicure and pedicure",
    "a delicate layered necklace",
    "oversized sunglasses",
    "a statement watch"
]

surprise_accessory = random.choice(accessories)
print(f"✨ {name}, you should wear {outfit}.")
print(f"Your surprise accessory is: {surprise_accessory}! 💎")
style_score = random.randint(8, 10)
print(f"Runway score: {style_score}/10 🔥")
decision = input().strip().lower()

while True:
    decision = input("\nChoose: approve or restyle: ").strip().lower()

    if decision == "approve":
        print("✅ Look approved! You're ready to turn heads.")
        break
    elif decision == "restyle":
        new_accessory = random.choice(accessories)
        print(f"🔄 Try it with {new_accessory}.")
    else:
        print("Please choose approve or restyle.")
