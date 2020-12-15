print("Welcome to Exchange kiosk")
exchange_rate = float(input("Today THB-USD exchange rate: "))
usd = int(input("Enter $USD amount: "))
thb = int(usd * exchange_rate)
fee = thb * 0.02
net = int(thb - fee)
print("{0} USD = {1} THB, Fee = {2:.2f} THB \nNet {3} THB".format(usd,thb,fee,net))

bank_1000 = net // 1000
net = net % 1000
bank_500 = net // 500
net = net % 500
bank_100 = net // 100
net = net % 100
bank_50 = net // 50
net = net % 50
bank_20 = net // 20
net = net % 20
coin_10 = net // 10
net = net % 10
coin_5 = net // 5
net = net % 5
coin_2 = net // 2
net = net % 2
coin_1 = net // 1
net = net % 1

print("Bank note and coin:")
print("Banknote 1000: ",bank_1000)
print("Banknote 500: ",bank_500)
print("Banknote 100: ",bank_100)
print("Banknote 50: ",bank_50)
print("Banknote 20: ",bank_20)
print("Coin 10: ",coin_10)
print("Coin 5: ",coin_5)
print("Coin 2: ",coin_2)
print("Coin 1: ",coin_1)