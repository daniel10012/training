'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

string = input("input a string")

words_list = string.split()
occurences = {}
for word in words_list:
    occurences[word] = words_list.count(word)

print(occurences)
print(max(occurences, key=lambda key: occurences[key]))




