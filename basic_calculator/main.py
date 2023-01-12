from art import logo
from replit import clear

# Add
def add(n1,n2):
  return n1 + n2

# Subtract
def subtract(n1,n2):
  return n1 - n2

# Multiply
def multiply(n1,n2):
  return n1 * n2

# Divide
def divide(n1,n2):
  return n1 / n2

operands = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():

  print(logo)
  
  calculate = True
  
  num1 = float(input('What is the first number: '))
    
  for symbol in operands:
    print(symbol)

  # Loop to continue program based on user inputs
  while calculate == True:
    symbol = input('Pick an operation from the line above: ')
    num2 = float(input('What is the second number: '))
    function = operands[symbol]
    answer = function(num1, num2)
    
    print(f'{num1} {symbol} {num2} = {answer}')
    
    stop = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type 'e' to end the program: ").lower()

    # How does the user want to continue
    # continue calculating using answer from before
    if stop == 'y':
      num1 = answer
      # Start program from beginning
    elif stop == 'n':
      calculate = False
      clear()
      calculator()
    else:
      # End Program
      calculate = False

calculator()