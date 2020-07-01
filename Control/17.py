# Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.

def calculator(num1, num2, op):
    if op=="+":
        return num1 + num2
    
    elif op=="*":
        return num1 * num2
    
    elif op=="-":
        return num1 - num2
    
    elif op=="/":
        try:
            val= num1 / num2
            return val
        except ZeroDivisionError:
            return "Math error , cannot divide by 0"
    
    else:
        print("Unsupportive Operand")
    

try:
    num1=int(input('Enter a first number'))
    num2=int(input('Enter another number'))
except ValueError:
    print("Enter numbers")

op= input("Enter an operand")

print(calculator(num1,num2,op))

