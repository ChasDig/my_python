def bubble_sort(array_):
    """
    Сортировка пузырьком.

    :param array_:
    :return:
    """
    n = len(array_)

    for i in range(n):
        swapped = False

        for j in range(n - i -1):
            if array_[j] > array_[j + 1]:
                array_[j], array_[j + 1] = array_[j + 1], array_[j]
                swapped = True

        if not swapped:
            break

    return array_
