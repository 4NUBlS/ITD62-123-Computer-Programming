def validate_person_id(pid):
    digit = 13
    answer = 0
    for i in range(0, 12):
        answer = answer + (int(pid[i]) * digit)
        digit -= 1
    check_digit = str(11 - (answer % 11))
    if check_digit[-1] == pid[12]: return True
    else: return False