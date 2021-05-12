import pytest

from app.fib import Fibonacci, ReversedFibonacci


@pytest.mark.parametrize('expected, iterator', [
    ([1, 2, 3, 5, 8, 13, 21, 34, 55], Fibonacci),
    ([21, 13, 8, 5, 3, 2, 1, 1, 0], ReversedFibonacci),
])
def test_iterable(expected, iterator):
    collection = iterator(10)
    result = [_ for _ in collection]
    assert expected == result[1:]
