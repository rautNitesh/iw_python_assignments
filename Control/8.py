# Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.

def is_prime(n):
    c=0
    for i in range(2,n//2+1):
        if n%i==0:
            c+=1
    if c>0:
        return False
    
    return True

try:
    n=int(input("Enter a num"))
except ValueError:
    print("Enter a number")

print(is_prime(n))