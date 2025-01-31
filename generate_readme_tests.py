init = """
from collections.abc import Callable
from typing import Any, Concatenate
from smart_decorator import simple_decorator, method_decorator, decorator

"""


def line_iter(f):
    for line in f:
        line: str
        yield line.rstrip()


with open("README.md", "r") as f:
    with open("test_readme.py", "w") as f2:
        f2.write(init)
        in_ = False
        it = line_iter(f)
        i = 0
        for line in it:
            if line.startswith("```python"):
                f2.write(f"\ndef test_readme_{i}():\n")
                i += 1
                in_ = True
            elif line.startswith("```"):
                if in_:
                    f2.write("   globals().update(locals())\n")
                in_ = False
            elif in_:
                f2.write(f"   {line}\n")
