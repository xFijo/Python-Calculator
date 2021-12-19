import os
import crayons
import time

multiply = '*'
plus = '+'
minus = '-'
pass
def clear():
    os.system('cls')
    print(crayons.green('Python Calculator By xFijo'))
    os.system("Title Python Calculator.")
pass
clear()
pass
print(crayons.cyan('\nFirst Number : '))
number1 = int(input())
print(crayons.green(f'Number [{number1}] Chosen.'))
pass
print(crayons.cyan('\nSecond Number : '))
number2 = int(input())
print(crayons.green(f'Number [{number2}] Chosen.'))
pass
def meth():
   method = input(crayons.cyan('\nEnter Method : [*] [-] [+] : '))
   print(crayons.green(f'Method [{method}] Chosen.'))
   time.sleep(1)
   if method == '*':
       print(crayons.green(f'{number1} * {number2} = {number1 * number2}'))
   elif method == '+':
       print(crayons.green(f'{number1} + {number2} = {number1 + number2}'))
   elif method == '-':
       print(crayons.green(f'{number1} - {number2} = {number1 - number2}'))
   else:
       print(crayons.red('Invalid Method.'))
pass
meth()
