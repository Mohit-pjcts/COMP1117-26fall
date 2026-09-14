from turtle import *

def draw_square(length):
    for _ in range(4):
        forward(length)
        left(90)

def draw_triangle(length):
    for _ in range(3):
        forward(length)
        left(120)

def serpinski(length, level):
    if level == 0:
        draw_triangle(length)
    else:
        for _ in range(3):
            serpinski(length=length//2, level=level-1)
            forward(length)
            left(120)


if __name__ == "__main__":
    pass
    # draw_square(100)
    
