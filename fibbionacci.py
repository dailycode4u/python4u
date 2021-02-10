"""from typing import Generator


def fib(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    first: int = 0
    last: int = 1
    for _ in range (1, n):
        first, last = last, first + last
        yield last

for i in fib(10):
    print(i)"""

