def add_tags(name,tag):
    print(f'<{tag}>{name}</{tag}>')


name=input("Enter your text\n")
tag= input("Enter the tag name you want your text to wrap around")

add_tags(name,tag)