# `Command` decorators allows to use function without parentheses

import asyncio

async def print_res(func):
    return str(await func)

class Command:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    def __await__(self):
        return print_res(self.func(*self.args, **self.kwargs)).__await__()
    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
