
# string functions



print("\n-- ##############\n")

username = input("What is your First Name? ")


print("\n-- ##############\n")


print(f"- Your name container {len(username)} Char.")



find_o_letter_index = username.find('o')

if(find_o_letter_index != -1):
    print(f"- Your username contain o chat at index {find_o_letter_index}")
else:
    print(f"- your name not container char o.")


print(f"- Your name capitalize is {username.capitalize()}")
print(f"- Your name upper is {username.upper()}")
print(f"- Your name lower is {username.lower()}")


print("\n-- ##############\n")

print(f"- Count of char o in your username is {username.count("o")}")

print(f"- replace char o with empty at your username is {username.replace("o"," ")}")


print(f"- is digit = {username.isdigit()}")
print(f"- is alpha = {username.isalpha()}")

print("\n-- ##############\n")


# index


print(f"- Index of 0 is = {username[0]}")
print(f"- Index of 1 is = {username[1]}")


print(f"- first two char of username is {username[0:2]}")

price = 2.3323

print(f"- print only two decimal digits is {price:.2f}")

print("\n-- ##############\n")
