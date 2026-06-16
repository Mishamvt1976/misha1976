original_list = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
unique_list = []
for item in original_list:
    if item not in unique_list:
       unique_list.append(item)
print(unique_list) 