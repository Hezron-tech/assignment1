def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
# Driver Code
duplicate = [5, 4, 5, 20, 5, 2, 20, 4]
print(Remove(duplicate))