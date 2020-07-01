# Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.

People=[]
People.append(("Nitesh","Raut",22))
People.append(("Hair","Poudel",None))
People.append(("Alan","Neupane",27))
People.append(("Ram","Neupane",27))
People.append(("Hari","Neupane",22))
People.append(("Rohit","Chand",None))
People.append(("Ram Kumar","Chand",22))
People.append(("Shyam","Shrestha",None))
age=0
n=0
for pep in People:
    if pep[2] is not None:
        age+=pep[2]
        n+=1
    
avg=age//n
print(n)
print(avg)
for pep in People:
    if pep[2] is not None:
        if pep[2]>avg:
            print(f"{pep[0]} Old")
        elif pep[2]==avg:
            print(f"{pep[0]} Same age")
        else:
            print(f"{pep[0]} Young")
    else:
        print("Can't determine")

