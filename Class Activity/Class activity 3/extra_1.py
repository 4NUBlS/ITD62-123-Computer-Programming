deposit = int(input("Enter Deposit : "))

if deposit > 100001:
    interest = deposit * 0.05
elif deposit >= 50001:
    interest = deposit * 0.04
elif deposit >= 10001:
    interest = deposit * 0.03
elif deposit >= 1:
    interest = deposit * 0.02
else:
    interest = 0

print("Interest = {0}".format(int(interest)))