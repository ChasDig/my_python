def linear_search(array_, target):
    """
    Линейный поиск элемента в массиве.

    :param array_:
    :param target:
    :return:
    """
    for i in range(len(array_)):
        if array_[i] == target:
            return i
    return None
