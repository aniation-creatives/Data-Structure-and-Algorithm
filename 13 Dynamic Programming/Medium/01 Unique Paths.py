from time_decorator import complexity_profiler


# @complexity_profiler
memo = {}
def unique_paths(m, n):
    key = (m, n)
    if key in memo:
        return memo[key]

    if m == 0 or n == 0:
        return 0
    elif m == 1 or n == 1:
        return 1

    memo[key] = unique_paths(m - 1, n) + unique_paths(m, n - 1)
    return memo[key]

m = 20
n = 20
print(unique_paths(m, n))  # Expected Output: 3
