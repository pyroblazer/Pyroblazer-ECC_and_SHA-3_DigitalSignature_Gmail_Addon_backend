import ecdsa
import random
from ecc import Point, Curve
import ecc
import util

def generate_z(message, curve : Curve):
    e_bits = bin(message)
    n_bits = bin(curve.n)
    Ln = len(e_bits)-len(n_bits)
    z_bin = e_bits[2:Ln+2] #let Z be the Ln leftmost bits of e, where Ln is the bit length of the group order n
    z = int(z_bin, 2)
    return z

def generate_k(n):
    return random.randrange(n)

def generate_s(k, z, r, private_key, n):
    return (z + r * private_key) * pow(k, -1) % n

def sign(message, private_key, curve : Curve):
    s = 0
    r = 0
    print(message)
    print(type(message))
    message = int(message,base=16)
    z = generate_z(message, curve)
    while(s ==0):
        while(r == 0):
            k = generate_k(curve.n)
            x = curve.G_x * k
            y = curve.G_y * k
            r = x % curve.n

        s = generate_s(k, z, r, private_key, curve.n)
    
    return Point(r,s)
     
def verify(message, signature, public_key, curve : Curve):
    # message = int(message,base=16)
    sign = signature.split("-")
    s = float(sign[1])
    r = float(sign[0])
    # Verify that r and s are integers in [1, n-1]. If not, the signature is invalid.
    if not (((r >= 1) and (r < curve.n)) and ((s >= 1) and (s < curve.n))):
        return False
    # convert output of hash into integer -> e
    print(message)
    print(type(message))
    message = int(message,base=16)
    # generate z
    z = generate_z(message, curve)
    # Calculate u1 = (z/s) mod n and u2 = (r/s) mod n
    s_pow_min1 = pow(s, -1)
    print("z = ",z)
    print("s_pow_min1 = ", s_pow_min1)
    print("curve.n = ", curve.n)
    u1 = (z * s_pow_min1) % curve.n
    u2 = (r * s_pow_min1) % curve.n

    Q = public_key.split("-")
    Q_x = int(Q[0])
    Q_y = int(Q[1])

    #Calculate the curve point (x1, y1) = u1 x G + u2 x Qa
    print("u1 = ",u1)
    print("G_x = ", curve.G_x)
    print("u2 = ",u2)
    print("Q_x = ",Q_x)
    x1 = u1 * curve.G_x + u2 * Q_x
    y1 = u1 * curve.G_y + u2 * Q_y
    # p1 = Point(u1 * curve.G_x, u1 * curve.G_y)
    # p2 = Point(u2 * curve.Q_x, u1 * curve.Q_y)

    # check r = x1 mod n
    v = x1
    #v = x1 % curve.n
    print("v = ", v)
    print("r = ", r)
    return (v == r)