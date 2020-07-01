# Write an if statement to determine whether a variable holding a year
# is a leap year.

def isLeapYear(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    return False

year=int(input("Enter year"))

print(isLeapYear(year))