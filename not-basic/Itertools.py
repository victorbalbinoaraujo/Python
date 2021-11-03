from itertools import combinations_with_replacement, product, permutations, combinations, accumulate, groupby
import operator

# Product
print("""
      Product
      """)
a = [1, 2]
b = [3, 4]

prod = product(a, b)
print(list(prod)) # [(1, 3), (1, 4), (2, 3), (2, 4)]

prod = product(a, b, repeat=2) 
print(list(prod)) # [(1, 3, 1, 3), (1, 3, 1, 4), (1, 3, 2, 3), (1, 3, 2, 4), (1, 4, 1, 3), (1, 4, 1, 4), (1, 4, 2, 3), (1, 4, 2, 4), (2, 3, 1, 3), (2, 3, 1, 4), (2, 3, 2, 3), 
                  # (2, 3, 2, 4), (2, 4, 1, 3), (2, 4, 1, 4), (2, 4, 2, 3), (2, 4, 2, 4)]



# Permutations
print("""
      Permutations
      """)
c = [1, 2, 3, 4]

perm = permutations(c)
print(list(perm)) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

perm = permutations(c, 2)
print(list(perm)) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]



# Combinations
print("""
      Combinations
      """)
d = [1, 2, 3, 4]

comb = combinations(d, 2)
print(list(comb)) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

comb_wr = combinations_with_replacement(d, 2)
print(list(comb_wr)) # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]


# Accumulate
print("""
      Accumulate
      """)
e = [1, 2, 3, 4, 5, 6]
accum = accumulate(e)

print(list(accum)) # [1, 3, 6, 10, 15, 21]

accum = accumulate(e, func=operator.mul)
print(list(accum)) # [1, 2, 6, 24, 120, 720]

e = [1, 2, 4, 6, 3, 2, 8, 7, 9]
accum = accumulate(e, func=max)

print(list(accum)) # [1, 2, 4, 6, 6, 6, 8, 8, 9]



# GroupBy
print("""
      GroupBy
      """)
f = [1, 2, 3, 4]

smaller_than_3 = lambda x: x < 3

group = groupby(f, key=smaller_than_3)

for key, value in group:
    print(key, list(value)) # True [1, 2]
                            # False [3, 4]

