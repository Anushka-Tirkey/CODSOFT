print("CALCULATOR")
print("Enter two numbers")
a=int(int(input("Enter first number\t")))
b=int(int(input("Enter second number\t")))
print("Choose an operation: \n1. Addition\t2. Subtraction\t3. Multiplication\t4. Division")
ch=int(input("Enter your choice\t"))
if ch==1:
    print(f'{a} + {b} = {a+b}')
elif ch==2:
    print(f'{a} - {b} = {a-b}')
elif ch==3:
    print(f'{a} * {b} = {a*b}')
elif ch==4:
    print(f'{a} / {b} = {a/b}')
else:
    print("Invalid input")