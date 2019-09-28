def linear_search(element, some_list):
    idxLocation = 0

    for i_idx in range(len(some_list)):
        if element == some_list[i_idx]:
            idxLocation = i_idx
            return idxLocation
    return "None"

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))