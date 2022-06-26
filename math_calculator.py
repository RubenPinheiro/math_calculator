import calculator_art
print(calculator_art.logo)

def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mult(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2

operation = {
  "+": add,
  "-": sub,
  "*": mult,
  "/": div
}

#THIS IS A FLAG

def calculator():
    should_continue = True

    num1 = float(input('What is the first number: '))
    for symbol in operation:
        print(symbol)

    while should_continue:
        
        operation_symbol = input("Pick an operation: ")
        num2 = float(input('What is the second number: '))
        answer = operation[operation_symbol](num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        if input(f'Type "y" if you want to keep calculating with the number {answer} or "n" for a new calculation \n') == 'y':
            num1 = answer
        else:
            calculator()
calculator()
