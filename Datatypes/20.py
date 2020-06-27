def check(items):
    count=0
    for item in items:
        if len(item)>2 and item[0]==item[len(item)-1]:
            count+=1
    return count

sample_list=['xyx','abc','aba','11221']
print(check(sample_list))
            