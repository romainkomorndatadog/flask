from flask.constants import MY_CONSTANT

def needless_nested_decorator(func):
     def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
     return wrapper


@needless_nested_decorator
def needless_decorator(func):
     def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
     return wrapper
     

