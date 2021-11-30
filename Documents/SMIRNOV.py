def decor(func):
    def dec(*args):
        print('Была вызвана функция [squ]')
        import time
        func(*args)
        return dec


@decor
def squ(length, amount):
    import math
    length = int(input("Enter length "))
    amount = int(input("Enter amount "))
    square = int((amount * length * length) / (4 * math.tan(math.pi / amount)))
    print('square = {square}')

@decor
def summator(num):
    num = int(input("enter the number"))
    sum = num
    while num > 0:
        num -= 1
        sum += num

    print({sum})