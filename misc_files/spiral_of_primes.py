import turtle
import random

from turtle import *

turtle.hideturtle() # Comment/Erase to see the turtle

def is_prime(n):
    if n == 1: return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


counter = 0
side = 1
size = 1000
colors = ["blue", "red", "green", "orange", "black", "purple"]

for i in range(2, size + 1):
    penup() # Comment/Erase to see lines
    forward(10)

    if is_prime(i):
        dot(5, random.choice(colors))

    counter += 1

    if counter == side:
        left(90)
        counter = 0
        if heading() in (90, 270):
            side += 1

turtle.done()
