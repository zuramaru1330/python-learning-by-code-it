def binary_search(element, some_list, start_index = 0, end_index = None):
    if end_index == None:
        end_index = len(some_list) - 1

    # put your code here

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))