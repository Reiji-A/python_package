# def memorize(f):
#     memo = {}
#     def _wrapper(n):
#         if n not in memo:
#             memo[n] = f(n)
#             print('hit')
#             print(memo)
#         return memo[n]
#     return _wrapper#

# @memorize
# def long_func(n):
#     r = 0
#     for i in range(10000000):
#         r += n * i
#     return r#

# for i in range(10):
#     #print(long_func(i))
#     long_func(i)#

# print("nextrun")
# for i in range(10):
#     print(long_func(i))

import functools
@functools.lru_cache()
def long_func(n):
    r = 0
    for i in range(10000000):
         r += n * i
    return r

for i in range(10):
    print(long_func(i))

print("nextrun")
for i in range(10):
    print(long_func(i))a
