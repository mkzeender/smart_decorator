from collections.abc import Callable
from typing import TYPE_CHECKING

from smart_decorator import simple_decorator
from sys import version_info

if TYPE_CHECKING:
    from typing import assert_type
else:

    def assert_type(*args, **kwargs):
        pass


@simple_decorator
def my_simple_decorator(func, option1: int = 10, option2: str = "default"):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + option1

    return wrapper


def test_with_parens():

    @my_simple_decorator(option1=12, option2="custom")
    def my_decorated_function(x: int, /) -> int:
        return x + 1

    assert_type(my_decorated_function, Callable[[int], int])

    assert my_decorated_function(1) == 14


def test_callback_style():

    def my_callback_function(x: int, /) -> int:
        return x + 1

    callback = my_simple_decorator(my_callback_function, 8, option2="True")

    assert callback(1) == 10

    assert_type(callback, Callable[[int], int])


def test_no_parens():

    @my_simple_decorator
    def my_decorated_function(x: int, /) -> int:
        return x + 1

    assert_type(my_decorated_function, Callable[[int], int])

    assert my_decorated_function(1) == 12
