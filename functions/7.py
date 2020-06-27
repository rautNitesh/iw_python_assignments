def calLowerUpper(s):
    clower=0
    cupper=0
    for i in s:
        if i.islower():
            clower+=1
        if i.isupper():
            cupper+=1
        
    return(cupper,clower)

s=input("Enter a string")
upper,lower=calLowerUpper(s)
print(f"No of uppercase:{upper}")
print(f"No of lowercase:{lower}")