'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

inv = float(input("investment"))
r = float(input("interest rate in percentage"))/100
n = float(input("number of years to invest"))

print(f"the future value is {inv*(1+r)**n}")