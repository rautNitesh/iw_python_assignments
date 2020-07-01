# Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?


l=list()
l.append('Ram')
print(id(l))
l.append('Hari')
l.append('Shyam')
l.append('Narayan')
l.append('Safal')
l.append('Bibek')
print(id(l))

l.sort()

print(l[0])
print(l[1])