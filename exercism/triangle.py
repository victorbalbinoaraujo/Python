def triangle(sides) -> bool:
    if(all(sides) > 0):
        a, b, c = sides[0], sides[1], sides[2]
        return (a + b >= c) and (a + c >= b) and (b + c >= a)

def equilateral(sides: list) -> bool:
    return len(set(sides)) == 1 if triangle(sides) else False

def isosceles(sides: list) -> bool:
    return len(set(sides)) <= 2 if triangle(sides) else False
    
def scalene(sides: list) -> bool:
    return len(set(sides)) == 3 if triangle(sides) else False

print(
    equilateral([2, 2, 2]),
    equilateral([2, 3, 2]),
    equilateral([0, 0, 0]),
    equilateral([0.5, 0.5, 0.5]),
)