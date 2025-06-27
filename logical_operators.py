
# logical operators AND , OR , NOT




print("\n-- ##############\n")

# or operator
temp = 25
is_raining= True

if is_raining or temp > 35 or temp < 0:
    print("- The outdoor event is cancelled today") 
else:
    print("- The outdoor event is still scheduled")


# and operator
temp = 35 
is_sunny = True

if is_sunny and temp >= 35:
    print("- It is hot today.")
    print("- It is sunny outside")
else:
    print("- The weather is cool")

# not operator 

is_sunny = False

if not is_sunny:
    print("- The weather is not sunny today")

print("\n-- ##############\n")
