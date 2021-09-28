print("             BMI CALCULATOR              ") #Heading Message

#take input for height and weight
height = float(input("Enter yoor height in (meter) : "))
weight = float(input("Enter you weight in (KG) : "))


BMI = round(weight / (height **2)) #Use round() to get round figure value

if BMI < 18.5:
    print(f"You BMI is {BMI}, You are Underweight.")
elif BMI < 25:
    print(f"You BMI is {BMI}, You have a normal weight.")
elif BMI < 30:
    print(f"You BMI is {BMI}, You are Overweight.")
elif BMI < 35:
    print(f"You BMI is {BMI}, You are Obese.")
else:
    print(f"You BMI is {BMI}, You are CLinically Obese.")