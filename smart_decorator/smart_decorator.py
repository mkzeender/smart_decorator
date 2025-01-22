from functools import wraps

from smart_decorator.utils import safe_wraps

_UNSET = object()


def decorator(dec_func):

    @wraps(dec_func)
    def smart_decorator_factory(func_or_pos_arg=_UNSET, *args, **kwargs):

        if callable(func_or_pos_arg):
            # called as a simple decorator or a normal function

            return safe_wraps(
                dec_func(func_or_pos_arg, *args, **kwargs), func_or_pos_arg
            )
        elif args and callable(args[0]):
            # To avoid ambiguity between @decorator and @decorator(argument),
            # we require the positional arguments to not be callable.
            raise TypeError(
                f"Positional argument in {dec_func.__name__} must not be callable"
            )
        elif func_or_pos_arg is _UNSET:
            # called as a decorator factory with no positional arguments

            def _smart_decorator(func):
                return safe_wraps(dec_func(func, *args, **kwargs), func)

            return _smart_decorator
        else:
            # called as a decorator factory with positional arguments
            def _smart_decorator(func):
                return safe_wraps(
                    dec_func(func, func_or_pos_arg, *args, **kwargs), func
                )

            return _smart_decorator

    return smart_decorator_factory
