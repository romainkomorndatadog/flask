print(f"I AM BEING IMPORTED {__file__=}")


def outer_decorator(func):
     def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
     return wrapper

@outer_decorator
def inner_decorator(func):
     def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
     return wrapper
