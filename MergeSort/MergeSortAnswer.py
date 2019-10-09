# 두 리스트 합치기
def merge(list1, list2):
    merged_list = []
    i = 0
    j = 0

    # 정렬되어 있는 list1과 list2의 원소들을 차례로 비교하여, 더 작은 원소를 merged_list에 추가하기
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # list1에 남은 원소가 있다면, merged_list에 추가하기
    if i < len(list1):
        while i < len(list1):
            merged_list.append(list1[i])
            i += 1

    # list2에 남은 원소가 있다면, merged_list에 추가하기
    if j < len(list2):
        while j < len(list2):
            merged_list.append(list2[j])
            j += 1

    return merged_list

# 합병 정렬
def merge_sort(my_list):
    # Base Case
    if len(my_list) <= 1:
        return my_list

    # Recursive Case: left와 right로 my_list를 나누어준다.
    left = my_list[:len(my_list) // 2]
    right = my_list[len(my_list) // 2:]

    # Recursive Case: my_list를 잘게 쪼개는 과정을 재귀적으로 반복하고, merge 함수를 사용하여 합쳐준다.
    return merge(merge_sort(left), merge_sort(right))

some_list = [11, 3, 6, 4, 12, 1, 2]
sorted_list = merge_sort(some_list)
print(sorted_list)