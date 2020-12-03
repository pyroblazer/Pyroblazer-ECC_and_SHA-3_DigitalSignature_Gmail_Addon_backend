import ecdsa
import random
from ecc import Point, Curve
import util


def sign(message, private_key, curve : Curve):
    s = 0
    r = 0
    while(s ==0):
        while(r == 0):
            k = random.randrange(n)
            x = int(curve.G_x * k)
            y = curve.G_y * k
            r = x % curve.n
        
        kmod = util.modinv(k, curve.n)
        s = (private_key * r * kmod) % curve.n
    
    return Point(r,s)
     
def verify(message, signature, public_key, curve : Curve):
    sign = signature.split("-")
    s = sign[1]
    r = sign[0]
    w = util.modinv(s, curve.n)
    u1 = w % curve.n
    u2 = (r * w) % curve.n

    Q = public_key.split("-")
    Q_x = Q[0]
    Q_y = Q[1]

    p1 = Point(u1 * curve.G_x, u1 * curve.G_y)
    p2 = Point(u2 * curve.Q_x, u1 * curve.Q_y)
    x = Curve.add_point(p1,p2)
    x_int = int(x.x)
    v = x_int % curve.n
    return (v == r)