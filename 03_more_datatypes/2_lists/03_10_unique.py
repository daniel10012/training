'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = []

for el in list_:
    if list_.count(el) == 1:
        unique_list.append(el)

print(unique_list)

rfc

