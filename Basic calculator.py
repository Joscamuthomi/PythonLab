#basic calculator

a = float(input("Enter the first No:"))

op = (input("Enter An operator(/, *, -, +):"))

b = float(input("Enter the sec No:"))

if op == "+":
    print(f"The answer is {a+b}")

elif op =="-":
    print(f"The answer is {a-b}")
    
elif op == "/":
    print(f"The answer is {a/b}")
    
elif op == "*":
    print(f"The answer is {a*b}")
    
else:
    print("Invalid operator")