
def addition_subtraction(a: int = 0 , b: int = 0, action: str = '+' ):
    if action == '-':
        return a - b

    return a + b

res = addition_subtraction(3, 7, '-')
print(res)