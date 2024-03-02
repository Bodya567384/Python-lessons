
while True:
    print('\n'*2, "Calculator [+ - * / ^] Exit: 'x' ")
    action = input('Action: ')
    if action == 'x':
        break
    elif action not in ('+', '-', '*', '/', '^'):
        continue

    n1 = float(input('Number 1:'))
    n2 = float(input('Number 2:'))

    if action == '+':
        result = n1 + n2

    elif action == '-':
        result = n1 - n2

    elif action == '*':
        result = n1 * n2

    elif action == '/':
        if n2 == 0:
            print("You can't do that")
            continue
        result = n1 / n2

    elif action == '^':
        result = n1 ** n2
    # else:
    #     print("Unknown command")
    print('Result = ', result)