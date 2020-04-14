from math import sqrt


# 输入一个正整数判断它是不是素数
def prime_number():
    num = int(input('请输入一个正整数：'))
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print('%d是素数' % num)
    else:
        print('%d不是素数' % num)


# 输入两个正整数计算他们的最大公约数和最小公倍数
def factor_number():
    x = int(input('x = '))
    y = int(input('y = '))
    # 如果 x 大于 y 就交换 x 和 y 的值
    if x > y:
        # 通过下面的操作将 y 的值赋值给 x，将 x 的值赋值给 y
        x, y = y, x
    # 从两个数中比较大的数开始做递减的循环
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            print('%d和%d的最大公约数是%d' % (x, y, factor))
            print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
            break


# 打印三角图案
def print_triangle():
    row = int(input('请输入行数：'))
    for i in range(row):
        for _ in range(i + 1):
            print('*', end='')
        print()
    print()
    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print(' ', end='')
            else:
                print('*', end='')
        print()
    print()
    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end='')
        for _ in range(2 * i + 1):
            print('*', end='')
        print()


if __name__ == '__main__':
    # prime_number()
    # factor_number()
    print_triangle()
