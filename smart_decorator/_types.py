from collections.abc import Callable
import sys
from typing import Any, Concatenate, TYPE_CHECKING, Protocol, overload


if sys.version_info >= (3, 12) or TYPE_CHECKING:

    type DecoratorFunctionType[
        DecoratedFunction, **DecoratorArgs, DecoratorReturnType
    ] = Callable[Concatenate[DecoratedFunction, DecoratorArgs], DecoratorReturnType]

    type Method[SelfT, **ArgT, ReturnT] = Callable[Concatenate[SelfT, ArgT], ReturnT]

else:

    class _GenericType:
        def __getitem__(self, item):
            return Method

    Method = DecoratorFunctionType = _GenericType()
