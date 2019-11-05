'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''

word = "AbbacUs"
vow_count = 0

lowcaseword = word.lower()
for letter in lowcaseword:
    if letter in ["a","e","i","o","u","y"]:
        vow_count += 1

print(vow_count)