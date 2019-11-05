'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

sentence = input("sentence")
symbol = input("symbol")
new_sentence = ""

f = sentence[0]
for letter in sentence:
    if letter == f:
        letter = symbol
    new_sentence += letter

print(new_sentence)
