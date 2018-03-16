def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
import math

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


    
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
    
    
def cal_numbers(*numbers):
    sum = 0
    for i in numbers:
        sum += i * i
    return sum
    
def person(name, age, *, city, job):
    print(name, age, city, job)

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)
move(3, 'A', 'B', 'C')