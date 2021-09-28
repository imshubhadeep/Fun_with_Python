''' RULES:----
 Write a short program that prints each number from 1 to 100 on a new line. 
 For each multiple of 3, print "Fizz" instead of the number. 
 For each multiple of 5, print "Buzz" instead of the number. 
 For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number. '''

X = int(input("Enter your range to play : "))
for number in range(1,X+1):
    if number%3 == 0 and number%5 == 0:
        print("Fizz Buzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else:
        print(number)