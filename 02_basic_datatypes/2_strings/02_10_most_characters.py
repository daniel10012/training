'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''

a,b,c = "seth", "aethsrjtset", "wre"

max_len = len(a)
for word in [a,b,c]:
    if len(word)>=max_len:
        max_word = word
print(max_word)