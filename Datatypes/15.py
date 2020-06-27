def insert_string_middle(name, text):
    if len(name) % 2 == 0:
        name1 = name[0:(len(name)//2)]
        name2 = name[len(name)//2:len(name)]
        return name1+text+name2
    else:
        return "Please enter even no of characters in the string"


name = input(
    "Enter string in which you want to insert another string in between")
text = input("Enter text you want to insert")
print(insert_string_middle(name, text))
