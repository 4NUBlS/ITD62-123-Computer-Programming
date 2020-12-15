def Temp():
    temp = float(input("Your Temp => "))
    if temp > 37.5:
        return True
    else:
        return False

print(Temp())