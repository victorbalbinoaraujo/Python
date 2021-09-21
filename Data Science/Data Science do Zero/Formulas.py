from collections import Counter
from math import sqrt
from functools import reduce

# Álgebra Linear
def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_sub(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_mul(v, w):
    return [v_i * w_i for v_i, w_i in zip(v, w)]

def vectors_sum(vectors):
    return reduce(vector_add, vectors)

def scalar_multiply(v, escalar):
    return [escalar * v_i for v_i in v]

def vectors_mean(vectors):
    return scalar_multiply(vectors_sum(vectors), 1/len(vectors))

def dot(v, w):
    return sum(vector_mul(v, w))

def sum_of_squares(v):
    return dot(v, v)

def magnitude(v):
    return sqrt(sum_of_squares(v))

def distance_vectors(v, w):
    return magnitude(vector_sub(v, w))



# Estatística
def mean(x):
    return sum(x) / len(x)

def median(x):
    pts = len(x)
    s = sorted(x)
    
    midpoint = pts // 2
    
    if midpoint % 2 == 1:
        return s[midpoint]
    
    else:
        low = midpoint - 1
        high = midpoint
        
        return (s[low] + s[high]) / 2
    
def trim_mean(x, n):
    
    x.sort()
    x = x[n:-n]
    
    return mean(x)

def quantile(x, p):
    
    p_idx = int(p * len(x))
    
    return sorted(x)[p_idx]

def mode(x):
    counts = Counter(x)
    
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count], max_count

def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    
    x_bar = mean(x)
    
    return [x_i - x_bar for x_i in x]

def variance(x):
    
    n = len(x)
    deviations = de_mean(x) 
    return sum_of_squares(deviations) / n 

def standard_deviation(x):
    return sqrt(variance(x))

def median_absolute_deviation(x):
    
    deviations = de_mean(x)
    x = [abs(x_i) for x_i in deviations]
    
    return sum(x) / len(x)