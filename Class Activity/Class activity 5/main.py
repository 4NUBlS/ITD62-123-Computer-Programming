loopWhile = 1
lotto_list = []

while loopWhile < 11:
    hue = int(input("Hue 3 Number => [ {0} ] => ".format(loopWhile)))
    if len(str(hue)) != 3:
        print("Please Input 3 Number Bro!!")
        continue
    lotto_list.append(hue)
    loopWhile += 1
else:
    print(lotto_list)