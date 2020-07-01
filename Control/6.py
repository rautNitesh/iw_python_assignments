# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

l=["Nitesh",'Hari','Shyam','Ram','Ramesh','Sonam','Bibek','Gaurab','Nabin','Dipesh']
name=input("Enter name to search\n")

def isNamePresent(name,l):
    for item in l:
        if item==name:
            return "Name found"

    return "Not Found"


print(isNamePresent(name,l))