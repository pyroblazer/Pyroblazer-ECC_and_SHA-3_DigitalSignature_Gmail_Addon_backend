import random
from math import sqrt
from util import is_prime
from ecc import Point, Curve

def generate_private(n) :
    i = random.randrange(2,n)
    while(not is_prime(i)):
        i = random.randrange(2, n)

    return i
    
def generate_public(private_key) :
    curve = Curve(0, 7, 11, None, None, 13)
    curve.generate_field()
    return Point(private_key * curve.G_x, private_key * curve.G_y)
    pass