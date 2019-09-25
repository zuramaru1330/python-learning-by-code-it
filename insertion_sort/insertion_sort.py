# insertion sorting
# please refer this code to pythontutor.com
def insertion_sort(my_list):
    for i_idx in range(len(my_list)):
        key = my_list[i_idx]
        count = 0

        while count < len(my_list[:i_idx]):
            if my_list[i_idx] < key:
                count += 1
            else:
                my_list[i_idx] = my_list[i_idx -1]
                my_list[i_idx -1] = key
                count += 1

    return my_list

some_list = [11, 3, 6, 4, 12, 1, 2]
insertion_sort(some_list)
print(some_list)