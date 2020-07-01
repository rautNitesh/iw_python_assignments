# Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.

def is_palindrome(name):
    if name==name[::-1]:
        return "Palindrome"
    return "Not palindrome"


name=input("Enter a string\n")
print(is_palindrome(name.lower()))