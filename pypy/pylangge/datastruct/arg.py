
import functools


def cache_results(func):
    memo = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Using args directly as part of the dict key fails if any item is unhashable
        key = (args, tuple(sorted(kwargs.items())))
        print("args : ", args, "typeof args : ", type(args), "kwargs : ", kwargs)

        if key not in memo:
            memo[key] = func(*args, **kwargs)
        return memo[key]

    return wrapper


@cache_results
def sum_items(nums, num1, num2):
    return sum(nums)


print(sum_items((1, 2, 3), 1, 2))

print(sum_items([1, 2, 3], 1, 2))
print(sum_items((1, 2, 3), 1, 2))  # Works: tuple is hashable -> 6
print(sum_items([1, 2, 3], 1, 2))
