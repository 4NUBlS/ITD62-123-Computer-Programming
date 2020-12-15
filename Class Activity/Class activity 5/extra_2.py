score_list = [3.6, 5.5, 8.7, 9.9, 10.0]
alls = 0.0
total = 0

for i in score_list:
    if i < 9.0:
        total += 1
        alls = alls + i
average = alls/total
print("Score < 9 = [ {0} ] | Average => {1:.2f}".format(total,average))