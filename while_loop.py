
# while loop

print("\n-- ##############\n")


name = input("- What is your name? ")

print("\n-- ##############\n")

while name == "":
    print("- You didn't enter your name.")
    name = input("- What is your name? ")

print(f"- Hello {name}")


# while loop up to ten
print("\n-- ##############\n")

i = 0 

while i < 5:
    i+=1
    print(f"- {i}")

print("\n-- ##############\n")
