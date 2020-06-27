def occurence(name):
    dict = {}
    list = name.split(" ")
    for item in list:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    return dict


name = input("Enter a sentence")
print(occurence(name))
