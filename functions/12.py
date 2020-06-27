def mul(n):
    def inner_function(b):
        return n*b
    return inner_function

try:
    n=int(input("Enter a num"))
    b=int(input("Enter unknown number"))
    result=mul(n)
    print(result(b))
except ValueError:
    print("Please, enter number")