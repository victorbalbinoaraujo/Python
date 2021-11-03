from collections import Counter, namedtuple, OrderedDict, defaultdict

# Counter
print("""
      Counter
      """)
a = "aaaabbbbbbbcccccc"
count = Counter(a)
print(count) # Counter({'b': 7, 'c': 6, 'a': 4})
print(list(count.elements())) # ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c']
print(count.values()) # dict_values([4, 7, 6])
print(count.most_common(1)[0][0]) # b
 


# Named Tuple
print("""
      Named Tuple
      """)
Point = namedtuple('Point', 'x,y')
pt = Point(1, 4) 
print(pt) # Point(x=1, y=4)
print(pt.x, pt.y) # 1 4



# Ordered Dict
print("""
      Ordered Dict
      """)
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['a'] = 1
ordered_dict['c'] = 3

print(ordered_dict) # OrderedDict([('b', 2), ('a', 1), ('c', 3)])



# Default Dict
print("""
      Default Dict
      """)
d = defaultdict(list)
d['a'] = 1
d['b'] = 2

print(d['a']) # 1
print(d['b']) # 2
print(d['c']) # []
