# python calculator

operator = input("- Enter an operator (+ - * /)? ")
n1 = float(input("- Enter the first Number? "))
n2 = float(input("- Enter The second Number? "))


if operator == "/":
    result= n1/n2
elif operator == "*":
    result = n1*n2
elif operator == "+":
    result = n1 + n2
elif operator == "-":
    result = n1 -n2
else:
    print(f"- Please Enter the operator of (+ - * /)")


print("\n-- ##############\n")

if result: 
    print(f"- Result is { round(result,2)}")
print("\n-- ##############\n")
