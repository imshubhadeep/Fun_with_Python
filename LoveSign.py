#Play with List in Python
r1 = ["💛","💚","💙"]
r2 = ["💛","💚","💙"]
r3 = ["💛","💚","💙"]

map = [r1,r2,r3] #Here nested list for making a map.
print(f"{r1}\n{r2}\n{r3}")
position = input("Enter your place: ") #This input is in "string" type.

Horizonal = int(position[0]) #Replace 👆 input in "int" type and specify
Vertical = int(position[1])  #the position in horizonal and vertical.

map[Vertical -1][Horizonal -1] = "💔"

print(f"{r1}\n{r2}\n{r3}")  #Print final outcome.