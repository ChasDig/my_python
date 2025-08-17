"""
Kiss (Keep It Simple, Stupid) - сложность должна быть оправдана.
"""

def bad_example_multiply_by_two(value: int) -> int:
    return value << 1


def good_example_multiply_by_two(value: int) -> int:
    return value * 2
