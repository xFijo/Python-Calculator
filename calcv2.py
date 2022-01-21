import os
import crayons

def clear():
  os.system('cls')
  print(crayons.green('Python Calculator By xFijo'))
  os.system("Title Python Calculator.")

pass
clear()
pass

while True:
  command = input(crayons.cyan("Enter Method [-] [*] [+] : ")).lower()
  args = command.split(' ')
  split = args[1:]
  content = " ".join(split)
  
  if command.startswith('+'):
    print(crayons.cyan('\nFirst Number : '))
    number1 = int(input())
    print(crayons.green(f'Number [{number1}] Chosen.'))
    pass
    print(crayons.cyan('\nSecond Number : '))
    number2 = int(input())
    print(crayons.green(f'Number [{number2}] Chosen.'))
    pass  
    print(crayons.green(f'{number1} + {number2} = {number1 + number2} \n\n\n'))

    pass

  elif command.startswith('-'):
      print(crayons.cyan('\nFirst Number : '))
      number1 = int(input())
      print(crayons.green(f'Number [{number1}] Chosen.'))
      pass
      print(crayons.cyan('\nSecond Number : '))
      number2 = int(input())
      print(crayons.green(f'Number [{number2}] Chosen.'))
      pass  
      print(crayons.green(f'{number1} - {number2} = {number1 - number2} \n\n\n'))
      pass

  elif command.startswith('*'):
      print(crayons.cyan('\nFirst Number : '))
      number1 = int(input())
      print(crayons.green(f'Number [{number1}] Chosen.'))
      pass
      print(crayons.cyan('\nSecond Number : '))
      number2 = int(input())
      print(crayons.green(f'Number [{number2}] Chosen.'))
      pass  
      print(crayons.green(f'{number1} * {number2} = {number1 * number2} \n\n\n'))
      pass

