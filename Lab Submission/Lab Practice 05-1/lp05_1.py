import numpy as np


def process_type():
    chart = np.array([16, 19, 21, 23, 26, 28, 30, 33, 35, 37, 40, 42])
    while True:
        type_ticket = int(input("MRT blue line ticket machine\nPress 1 for Adult ticket\nPress 2 for Elder/Child ticket\nPress 3 for Student ticket\n: "))
        if type_ticket == 1:
            return chart
        elif type_ticket == 2:
            for i in range(0, 12):
                chart[i] = chart[i] - (chart[i] * 0.50) + 0.5
            return chart
        elif type_ticket == 3:
            for i in range(0, 12):
                chart[i] = chart[i] - (chart[i] * 0.10) + 0.5
            return chart
        else:
            print("\nInput 1 or 2 or 3\n")
            continue


def process_station():
    chart_select = process_type()
    while True:
        select_station = int(input("Please select station (0-18): "))
        if 0 <= select_station <= 1:
            return chart_select[0]
        elif 2 <= select_station <= 11:
            return chart_select[select_station-1]
        elif 12 <= select_station <= 18:
            return chart_select[11]
        else:
            print("\nInput 0-18\n")
            continue


def process_coin():
    fare = process_station()
    print("Fare = {0} THB".format(fare))
    while True:
        insert_coin = int(input("Please insert banknote/coin: "))
        if insert_coin >= fare:
            print("Change {0} THB\nGet your ticket, Thanks you".format(
                insert_coin - fare))
            break
        elif insert_coin < fare:
            print("Require more cash....")
            continue
