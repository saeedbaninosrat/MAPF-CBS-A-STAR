def find_lists_with_same_element_at_index(lists):
    lists_to_ignore = []
    longest_list_length = max(map(len, lists))
    print(longest_list_length)
    list1 = {}
    for index in range(longest_list_length):
        list1[index] = {}
        dic1 = {}
        for list_number, list_context in enumerate(lists, 1):
            if index < len(list_context):
                element = list_context[index]
                if element not in dic1:
                    dic1[element] = []
                dic1[element].append(f"list{list_number}")
        for k,v in dic1.items():
            if len(v) > 1:
                list1[index][k] = v
        print(index, list1[index])
    return    
            
    
# Example lists
list1 = [1, 2, 4, 4, 5]
list2 = [1, 6, 3, 4, 5]
list3 = [1, 3, 4, 9, 10]
list4 = [1, 3, 11]
list5 = [1, 3, 4, 12]
list6 = [1, 2, 1, 4, 5]
list7 = [1, 6, 7, 8]
list8 = [1, 3, 4, 9, 10]
list9 = [1, 3, 11]
list10 = [1, 3, 1, 12,13]

lists = [list1, list2, list3, list4, list5, list6, list7, list8, list9, list10]
results = find_lists_with_same_element_at_index(lists)
