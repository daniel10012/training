'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

sentence = "hello world"
l = "o"
index = 0

for letter in sentence:
    if letter == l:
        break
    index += 1

print(index)

