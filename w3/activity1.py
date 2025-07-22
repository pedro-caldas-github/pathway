# temperature = float(input("What is your temperature?\n"))

# if temperature > 40.5:
#     print("Go to the hospital NOW!")
# elif temperature > 39.5:
#     print("Call the doctor!")
# else:
#     print("You are good!!")

num1 = int(input("input the first number:\n"))
num2 = int(input("input the second number:\n"))
animal = "Monkey"

if num1 > num2:
    print(f"the number {num1} is greater than {num2}")
elif num1 == num2:
    print("both numbers are equal")
else:
    print(f"{num2} is greater than {num1}")

friend_favorite_animal = input("Hey, what is your favorite animal?\n")

if friend_favorite_animal.title() == animal:
    print("Hey thats my favorite animal too!!!")
else:
    print("this is one of my favorite animals!!!")
