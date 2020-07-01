# Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.
# For the data in the previous example it would return:
# [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
# 'John', 'address': '54 Love Ave', 'age': 21}]
import csv
def read_csv(filename):
    output=[]
    with open (filename+'.csv','r')as f:
        reader=csv.reader(f)
        header=next(reader)
        for row in reader:
            output.append(dict(zip(header,row)))

       
    return output

print(read_csv('nites'))
