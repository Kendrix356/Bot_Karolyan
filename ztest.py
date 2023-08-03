def custom_sort(arr):
    count_dict = {}
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1
    has_duplicates = any(count > 1 for count in count_dict.values())
    if not has_duplicates:
        return arr
    def custom_key_func(element):
        return (-count_dict.get(element, 0), element)
    sorted_arr = sorted(arr, key=custom_key_func)
    return sorted_arr

arr_without_duplicates = ["1","2","2"]
sorted_arr_without_duplicates = custom_sort(arr_without_duplicates)
print(sorted_arr_without_duplicates)  # Вывод: [3, 1, 4, 5, 9, 2, 6]
