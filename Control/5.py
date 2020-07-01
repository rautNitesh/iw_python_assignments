# Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

People=[]
People.append(("Nitesh","Raut",22))
People.append(("Hair","Poudel",23))
People.append(("Alan","Neupane",27))
People.append(("Rohit","Chand",26))

People.sort(key= lambda x:x[0])
print(People)

People.sort(key= lambda x:x[1])
print(People)

People.sort(key= lambda x:x[2])
print(People)
