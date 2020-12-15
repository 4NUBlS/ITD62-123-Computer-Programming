def cal_average(score_list):
    alls = 0.0

    for i in score_list:
        alls = alls + i
    average = alls/len(score_list)
    return average

score_list = [3.6, 5.5, 8.7, 9.9, 10.0]
print("Average => {0:.2f}".format(cal_average(score_list)))