'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

list = [2,3,1]
l = list[0]
for i in range(len(list)):
    if list[i]>=l:
        l=list[i]

print(l)


p=1
for n in list:
    p *= n
print(p)