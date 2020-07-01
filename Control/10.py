# Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.

def convertCase(s,snake):
    l=[s[0].lower()]
    for i in s[1:]:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            l.append(snake)
            l.append(i.lower())
        else:
            l.append(i)

    l="".join(l)

    print(l)

snake="_"
kebab="-"
convertCase("RamHariShyam",snake)


