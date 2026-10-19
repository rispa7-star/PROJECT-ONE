num1 = float(input("Enter first number: "))
operator = ("+,-,*,/") # I have assigned the operator the operators so that they dont keep appearing on my terminal input
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))
# the input is to ask the user for data or insert data

if operator == "+":
    print("Answer:",  num1 + num2) 
elif operator =="*":
    print("Answer:", num1 * num2)        # remember to change the operator as well.. For ans 50 its because i did not change now for and 400 its because i changed.
elif operator =="-":
    print("Answer:", num1 - num2)
elif operator =="/":
    if num2 != 0:
        print("Answer:", num1/num2)
    else:
        print("Answer:", "Cannot be divided by zero") 



