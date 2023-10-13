# Sum and multiplication function


def sum_function_two_numbers(a, b):
    return a + b


def multiplication_two_numbers(a, b):
    return a * b


def create_decorator(operator):
    def decorator(func):
        def wrapper(a, b):
            print(f'Operação de {operator}')
            result = func(a, b)
            return result
        return wrapper
    return decorator


@create_decorator('sum')
def sum_function(input_sum_a, input_sum_b):
    return sum_function_two_numbers(input_sum_a, input_sum_b)


@create_decorator('multiply')
def multiply_function(input_multiply_a, input_multiply_b):
    return multiplication_two_numbers(input_multiply_a, input_multiply_b)


result_sum = sum_function(4, 10)
print(result_sum)
result_multiply = multiply_function(5, 5)
print(result_multiply)
