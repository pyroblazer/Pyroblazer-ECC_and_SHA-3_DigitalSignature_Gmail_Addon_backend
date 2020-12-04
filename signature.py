import ecdsa
import random
from ecc import Point, Curve
import ecc
import util


def sign(message, private_key, curve : Curve):
    s = 0
    r = 0
    message = int(message,base=16)
    z = len(str(message))-1 #let Z be the Ln leftmost bits of e, where Ln is the bit length of the group order n
    n = str(message)[:z]
    while(s ==0):
        while(r == 0):
            kmod = None
            while(kmod is None):
                k = random.randrange(int(n))
                kmod = util.modinv(k, curve.n)
            x = int(curve.G_x * k)
            y = curve.G_y * k
            r = x % curve.n

        #print(type(kmod))
        s = (z + r * kmod) % curve.n
    
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