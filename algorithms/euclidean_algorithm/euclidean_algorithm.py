def gcd(first, second):
    """
    Нахождение НОД двух чисел с помощью алгоритма Евклида.

    :param first:
    :param second:
    :return: НОД
    """
    while second:
        first, second = second, first % second

    return first
