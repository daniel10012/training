'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5, 5,6,2,9,4,3,6,9]


# s = set(list_)
# l = list(s)
# print(l)

single_list = []
for num in list_:
    if num not in single_list:
        single_list.append(num)

print (single_list)