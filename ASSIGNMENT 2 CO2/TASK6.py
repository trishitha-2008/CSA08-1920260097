# Recursion and Its Limits

from functools import lru_cache
import sys

calls = 0


def ways_naive(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


# Naive and memoised versions
calls = 0
print("Naive:", ways_naive(25), "Calls:", calls)

calls = 0
ways_memo.cache_clear()
print("Memoised:", ways_memo(25), "Calls:", calls)


# Answers for steps 1 to 6
print("\nAnswers from 1 to 6:")

for n in range(1, 7):
    print(n, "steps:", ways_memo(n))


# Compare function calls
print("\nFunction call comparison:")

for n in [10, 20, 25, 30]:
    calls = 0
    ways_naive(n)
    naive_calls = calls

    calls = 0
    ways_memo.cache_clear()
    ways_memo(n)
    memo_calls = calls

    print(n, "steps:", "Naive calls =", naive_calls,
          "| Memoised calls =", memo_calls)


# Recursion limit
print("\nRecursion limit:", sys.getrecursionlimit())

try:
    print("Ways for 1000 steps:", ways_memo(1000))
except RecursionError:
    print("RecursionError: Maximum recursion depth exceeded")


# Iterative solution
def ways_iterative(n):
    if n <= 1:
        return 1

    first = 1
    second = 1

    for i in range(2, n + 1):
        first, second = second, first + second

    return second


print("\nIterative result for 1000 steps:")
print(ways_iterative(1000))
