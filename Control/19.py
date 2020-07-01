def check_balance(n):
    open = "({["
    close = ")}]"
    l = []
    for i in n:
        if i in open:
            l.append(i)
        elif i in close:
            if l[len(l)-1] == open[0] and i == close[0]:
                l.pop()
            elif l[len(l)-1] == open[1] and i == close[1]:
                l.pop()
            elif l[len(l)-1] == open[2] and i == close[2]:
                l.pop()
            else:
                return False
        else:
            return 'Enter valid parantheses'
    if len(l) == 0:
        return True
    return False


n = "{}([])[[[{{{}}}]]]"
print(check_balance(n))
