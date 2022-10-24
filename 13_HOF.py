from unittest import result


def increment(x):
    return x + 1

increment_v2 = lambda x: x + 1
def high_ord_func(x, func):
    return x + func(x)

high_ord_func_v2 = lambda x, func: x + func(x)

result = high_ord_func(2, increment)
result2 = high_ord_func_v2(4, increment_v2)
result3 = high_ord_func_v2(4, lambda x: x + 2)
print(result)
print(result2)
print(result3)