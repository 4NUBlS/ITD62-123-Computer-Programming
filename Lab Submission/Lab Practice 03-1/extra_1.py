MyList = []
line = "-----------------------------------"

for i in range(1, 11):
    MyList.append(float(input("Enter GPAX of Student No.{0}: ".format(i))))

print(MyList,"\n",line)
print("Average of GPAX: {0:.2f}".format((MyList[1] + MyList[2] + MyList[4]) / 3),"\n",line)
print("Max GPAX: {0:.2f}".format(max(MyList)),"\n",line)
print("Min GPAX: {0:.2f}".format(min(MyList)),"\n",line)