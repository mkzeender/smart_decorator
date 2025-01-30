from collections.abc import Callable
from typing import Any, Concatenate, Protocol, overload
from smart_decorator.types import DecoratorFunctionType, Method
from smart_decorator.smart_decorator import _SmartDecoratorFactory

def method_decorator[
    InputSelf, **InputArgs,
    InputReturn,
    OutputSelf, **OutputArgs,
    OutputReturn, **DecoratorArgs,
](
    dec_func: DecoratorFunctionType[
        Callable[Concatenate[InputSelf, InputArgs], InputReturn],
        DecoratorArgs,
        Method[OutputSelf, OutputArgs, OutputReturn],
    ]
) -> _Tmp[InputArgs, InputReturn]: ...

# ) -> _MethodDecoratorFactory[
#     InputSelf,
#     InputArgs,
#     InputReturn,
#     OutputSelf,
#     OutputArgs,
#     OutputReturn,
#     DecoratorArgs,
# ]: ...

class _Tmp[**Params, Ret]: ...

class _MethodDecoratorFactory[
    InSelf, **InArgs, InRet, OutSelf, **OutArgs, OutRet, **DecArgs
](Protocol):
    ...
    # @overload
    # def __call__(
    #     self,
    #     func: Method[InSelf, InArgs, InRet],
    #     *args: DecArgs.args,
    #     **kwargs: DecArgs.kwargs,
    # ) -> DecoratedMethod[OutSelf, OutArgs, OutRet]: ...
    # @overload
    # def __call__(
    #     self,
    #     func: Callable[InArgs, InRet],
    #     *args: DecArgs.args,
    #     **kwargs: DecArgs.kwargs,
    # ) -> Callable[OutArgs, OutRet]: ...
    # @overload
    # def __call__(
    #     self, *args: DecArgs.args, **kwargs: DecArgs.kwargs
    # ) -> _MethodDecorator[InSelf, InArgs, InRet, OutSelf, OutArgs, OutRet]: ...

class _MethodDecorator[InSelf, **InArgs, InRet, OutSelf, **OutArgs, OutRet](Protocol):
    @overload
    def __call__(
        self, func: Method[InSelf, InArgs, InRet], /
    ) -> DecoratedMethod[OutSelf, OutArgs, OutRet]: ...
    @overload
    def __call__(
        self, func: Callable[InArgs, InRet], /
    ) -> Callable[OutArgs, OutRet]: ...

class DecoratedMethod[SelfType, **ArgsType, ReturnType](Protocol):
    def __call__(
        self, first_arg: SelfType, /, *args: ArgsType.args, **kwargs: ArgsType.kwargs
    ) -> ReturnType: ...
    @overload
    def __get__(
        self, instance: None, owner: Any = None
    ) -> Callable[Concatenate[SelfType, ArgsType], ReturnType]: ...
    @overload
    def __get__(
        self, instance: SelfType, owner: Any = None
    ) -> Callable[ArgsType, ReturnType]: ...
