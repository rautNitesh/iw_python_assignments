add= lambda x: x+15
mul= lambda x,y:x*y

try:
    a=int(input("Enter number to add & mul function"))
    b=int(input("Enter number to mul function"))
    print(add(a))
    print(mul(a,b))
except ValueError:
    print("Enter numbers as input")