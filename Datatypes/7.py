def length(list):
    max=len(list[0])
    for item in list:
        l=len(item)
        if l>max:
            max=l
    return max

print(length(['nitesh','raut','kshettriake','haminepali']))
