print("Body Mass Index (BMI) Calculator")
weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(M): "))
line = "--------------------------------------"
bmi = weight / (height ** 2)

if bmi >= 30:
    print("{0}\nBMI = {1:.2f}. You are Obese.\n{2}".format(line,bmi,line))
elif bmi >= 25:
    print("{0}\nBMI = {1:.2f}. You are Overweight.\n{2}".format(line,bmi,line))
elif bmi >= 18.5:
    print("{0}\nBMI = {1:.2f}. You are Healty.\n{2}".format(line,bmi,line))
elif bmi < 18.5:
    print("{0}\nBMI = {1:.2f}. You are Underweight.\n{2}".format(line,bmi,line))