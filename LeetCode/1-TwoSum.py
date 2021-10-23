from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    dic = {}
    for idx, n in enumerate(nums):
        if (target - n) in dic:
            return [dic[target - n], idx]
        dic[n] = idx

print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4,7,9,14,28], 11))
print(two_sum([3,3,7,14,21,25], 46))
print(two_sum([3,5,8,12,14,18,23,25], 48))