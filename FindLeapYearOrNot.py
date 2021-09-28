print("             FIND LEAP YEAR OR NOT              ") #Heading Message

# Conditions is when year divide by 100 and not divisible by 4 or 400 then it's not a leap year.
def leapyear(year):
    if ((year%4 !=0) or ((year%400 !=0) and (year%100 == 0))):
        print("This is not a leap year.")
    else:
        print("This is a leap year.")

year = int(input("Enter the year : "))
leapyear(year)

''' Also we can write like this -->
 leapyear(int(input("Enter your Year : ")))'''