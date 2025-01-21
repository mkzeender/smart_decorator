from collections.abc import Callable
from typing import Concatenate, Never, Protocol, overload

# This overload blocks the 2nd positional argument from being a Callable
# This would cause ambiguity as to whether we are using it as a decorator or a factory.
# @overload
# def decorator[
#     **OptionType, **ParamType, ReturnType
# ](
#     dec_func: Callable[
#         Concatenate[Callable[ParamType, ReturnType], Callable, OptionType],
#         Callable[ParamType, ReturnType],
#     ]
# ) -> SmartDecoratorFactory[OptionType, Never, Never]: ...
# @overload
def decorator[
    **OptionType, CallableInput: Callable, CallableOutput: Callable
](
    dec_func: Callable[Concatenate[CallableInput, OptionType], CallableOutput]
) -> SmartDecoratorFactory[OptionType, CallableInput, CallableOutput]: ...

class SmartDecoratorFactory[**OptionType, CallableInput, CallableOutput](Protocol):
    @overload
    def __call__(
        self, *args: OptionType.args, **kwargs: OptionType.kwargs
    ) -> Callable[[CallableInput], CallableOutput]: ...
    @overload
    def __call__(self, func: CallableInput) -> CallableOutput: ...
