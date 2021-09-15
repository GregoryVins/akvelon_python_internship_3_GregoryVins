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
