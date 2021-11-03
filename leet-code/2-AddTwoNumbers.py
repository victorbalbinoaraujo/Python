from typing import List

def list_to_int(l1: List[int]) -> int:
    strings = [str(elem) for elem in reversed(l1)]
    join_str = "".join(strings)
    return int(join_str)

def int_to_list(integer: int) -> List[int]:
    int_str = str(integer)
    int_map = map(int, int_str)
    return list(int_map)

def add_two_numbers(l1: List[int], l2: List[int]) -> List[int]:
    l_int = list_to_int(l1) + list_to_int(l2)
    return (int_to_list(l_int)[::-1])
  
print(add_two_numbers([2,4,3], [5,6,4]))

