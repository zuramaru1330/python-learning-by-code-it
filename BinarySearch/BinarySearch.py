def binary_search(element, some_list):
    start_idx = 0
    end_idx = len(some_list) - 1
    mid_idx = int(len(some_list) / 2) - 1

    while start_idx <= end_idx:

        if some_list[mid_idx] == element:
            return mid_idx
        elif element >= some_list[mid_idx]:
            start_idx = mid_idx + 1
            mid_idx = start_idx
        elif element <= some_list[mid_idx]:
            end_idx = mid_idx - 1
            mid_idx = end_idx

    return "None"


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))