# Smart Decorator

A static-typed library for creating decorators.


```python
from typing import Callable
from smart_decorator import simple_decorator

_events = {}

@simple_decorator
def register(callback, *, event_type: str = 'normal'):
    _events[event_type] = callback
    return callback


@register # Parentheses optional
def on_normal():
    print('an event happened!')

@register(event_type='error')
def on_error():
    print('an error!')

# can be used as a normal function, too
def on_close():
    print('closing!')

register(on_close, event_type='close')

```