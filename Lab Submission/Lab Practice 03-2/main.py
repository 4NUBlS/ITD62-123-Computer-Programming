line = "---------------------------------------"
loop = 0
weight = []
height = []
weight_average = 0.0
height_average = 0.0

while True:
    children = int(input("Children record list...\nHow many children(s): "))
    if children > 20:
        print("\nChildren(s) Over 20\n")
        continue
    while children != loop:
        loop += 1
        print("{0}\nChildren #{1}".format(line,loop))
        weight.append(float(input("Enter weight(Kg): ")))
        height.append(float(input("Enter height(M): ")))
    for i in weight: weight_average = weight_average + i
    for i in height: height_average = height_average + i
    print("{0}\nAverage of weight = {1:.2f} Kg\nAverage of height = {2:.2f} M".format(line,weight_average / len(weight),height_average / len(height)))