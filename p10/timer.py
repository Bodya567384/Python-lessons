import time
a = 100

# define the countdown function
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        print_time = '{:02d}:{:02d}'.format(mins, secs)
        print(print_time)
        time.sleep(1)
        t -= 1

    print('End !!!')

t = int(input('Enter the time in seconds: '))
countdown(t)

print(a)