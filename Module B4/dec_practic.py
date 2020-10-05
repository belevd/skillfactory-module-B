def my_decorator(fn):
    answers_list = {}
    def wrapper(n):
        nonlocal answers_list
        if n not in answers_list:
            result = fn(n)
            answers_list[n] = result
            return result
        else:
            return answers_list[n]
    return wrapper

@my_decorator
def fn(n):
   return n * 123456789

print(fn(2))
print(fn(3))
print(fn(3))