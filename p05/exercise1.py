import random

# for i in range(5):
#     print(i, end=' ')
# print()
# for i in range(2, 5):
#     print(i, end=' ')
# print()
# for i in range(4, 11, 2):
#     print(i, end=' ')

# start = int(input('Start :'))
# end = int(input('End :'))
# step = int(input('Step :'))
#
# for x in range(start, end + 1, step):
#     print(x, end=', ')

# x = random.randint(0, 100)
# print(x)

# for i in range(101):
#     x = random.randint(0, 100)
#     print(x, end=' ')

# for j in range(1, 11):
#     print()
#     for i in range(1, 11):
#         print(f'{j}*{i}={j*i}', end=' ')

start_range = int(input('Start: '))
end_range = int(input('End: '))
for x in range(start_range, end_range + 1):
    is_prime = True

    for i in range(2, x):
        if x % i == 0:
            is_prime = False
            break

    if is_prime:
        print('%d, ' % x, end='')