import time


def countdown(t):
    while t:
        timeformat = '{:02d} Minutes Remaining!!!!'.format(t)
        print('\r{}'.format(timeformat), end='')
        time.sleep(60)
        t -= 1
    print('\nGoodbye!\n')


countdown(65)
