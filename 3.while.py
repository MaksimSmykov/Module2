my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
check_num = 0
while check_num < len(my_list):
    if my_list[check_num] > 0:
        print(my_list[check_num])
        check_num += 1
        continue
    elif my_list[check_num] < 0:
        break
    else:
        check_num += 1