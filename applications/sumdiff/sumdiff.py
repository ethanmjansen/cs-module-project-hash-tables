"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

sums = {}
diffs = {}

for i in q:
    for j in q:

        sum = f(i) + f(j)

        if sum in sums:
            sums[sum].append((i, j))
        else:
            sums[sum] = [(i, j)]

print(sums)