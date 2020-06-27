tuplex=1,2,3
t=input("Enter item\n")
try:
    val=int(t)
except ValueError:
    val=str(t)
tuplex+=(val,)
print(tuplex)