from .euclidean_algorithm import gcd


def test_euclidean_algorithm():
    assert gcd(48, 18) == 6
    assert gcd(1071, 462) == 21
