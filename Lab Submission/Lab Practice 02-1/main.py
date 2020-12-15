print("Diabetes measurement program")
dm = int(input("Enter blood sugar: "))
line = "-------------------------------"

if dm > 126:
    print("{0}\nBlood sugar = {1} mg/dL. You are risk.\n{2}".format(line,dm,line))
else:
    print("{0}\nBlood sugar = {1} mg/dL. You are normal.\n{2}".format(line,dm,line))