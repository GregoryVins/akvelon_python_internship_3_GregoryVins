def fibonacci(n: int):
    """
    Recursive function, be careful.
    :param n: number
    :type n: int
    :return: n’th number of Fibonacci sequence
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(0))  # 0
    print(fibonacci(1))  # 1
    print(fibonacci(2))  # 1
    print(fibonacci(3))  # 2
    print(fibonacci(4))  # 3
    print(fibonacci(5))  # 5
    print(fibonacci(6))  # 8
    print(fibonacci(7))  # 13
    print(fibonacci(8))  # 21
    print(fibonacci(9))  # 34
