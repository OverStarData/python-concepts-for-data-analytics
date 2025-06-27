# if statement 


# check age category
age = float(input("- How old are you? "))

print("\n-- ##############\n")

if age >=18:
    print(f"- You are now signed up")
elif age < 0:
    print(f"- You not born yet! ")
else:
    print(f"- You can't sign up! sorry")


# check if the user entered the name

name = input("- What is your name? ")

if name == "":
    print("- Please enter your name")
else:
    print(f"- Hello {name}")

print("\n-- ##############\n")

