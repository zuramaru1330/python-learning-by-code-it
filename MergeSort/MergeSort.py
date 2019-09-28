# 두 리스트 합치기
def merge(list1, list2):
    new_list = []
    i_idx = 0
    j_idx = 0

# 합병 정렬
def merge_sort(my_list):
    if list1[i] <= list2[j]:
        new_list.append(list1[i])
        i += 1
    else:
        new_list.append(list2[j])
        j += 1

some_list = [11, 3, 6, 4, 12, 1, 2]
sorted_list = merge_sort(some_list)
print(sorted_list)