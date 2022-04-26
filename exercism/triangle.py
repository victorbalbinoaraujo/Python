def triangle(sides) -> bool:
    if(all(sides) > 0):
        a, b, c = sides[0], sides[1], sides[2]
        return (a + b >= c) and (a + c >= b) and (b + c >= a)

def equilateral(sides: list) -> bool :
    if triangle(sides):
        return len(set(sides)) == 1
    return False

def isosceles(sides: list) -> bool:
    if triangle(sides):
        return len(set(sides)) <= 2
    return False
    
def scalene(sides: list) -> bool:
    if triangle(sides):
        return len(set(sides)) == 3
    return False

print(
    equilateral([2, 2, 2]),
    equilateral([2, 3, 2]),
    equilateral([0, 0, 0]),
    equilateral([0.5, 0.5, 0.5]),
)