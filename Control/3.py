# Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.
def isAnagram(str1, str2):
    if sorted(str1)==sorted(str2):
        return True 
    return False


def rtrAnagram(para):
    l= para.split(" ")
    l2=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if isAnagram(l[i],l[j]):
                l2.append(l[i])
                l2.append(l[j])
            
    return l2

para="the quick xof brown fox fried kciuq eth "
print(rtrAnagram(para))
