# Decorators are a very powerful and useful tool in Python since it allows programmers to 
# modify the behaviour of a function or class.
#  Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, 
#  without permanently modifying it.

# functional and class decorators
import functools
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("start")
        res = func(*args,*kwargs)
        print("End")
        return res
    return wrapper

# # @start_end_decorator
# # def print_name():
# #     print("Alex")

# @start_end_decorator
# def add(x):
#     return x+5

# # print_name = start_end_decorator(print_name)
# # print_name()

# # res = add(23)
# # print(help(add))
# print(add.__name__)
# print(res)

# import functools
# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kwargs):
#             for _ in range(num_times):
#                 res = func(*args,**kwargs)
#             return res
#         return wrapper
#     return decorator_repeat

def debug(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = " ,".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        res = func(*args,**kwargs)
        print(f"{func.__name__!r}) returned {res!r}")
        return res
    return wrapper

@debug
@start_end_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello('Prajwal')


# @repeat(num_times=3)
# def greet(name):
#     print(f"hello {name}")

# greet('Prajwal')

class CountCalls:
    def __init__(self,func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self,*args,**kwargs):
        # print('Hey,there')
        self.num_calls += 1 
        print(f"This is executed {self.num_calls} times")
        return self.func(*args,**kwargs)

# cc = CountCalls(None)
# cc()

@CountCalls
def hello():
    print("Hello")

hello()
hello()



