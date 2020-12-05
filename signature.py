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
    return (k**(-1) *(z + r * private_key)) % n

def test(C, u1, G, u2, QA, private_key, z,r,s):
    if (QA.x != (private_key * G.x)) or (QA.y != (private_key * G.y)):
        return False
    if (C.x != u1 * G.x + u2* private_key*G.x) or (C.y != u1 * G.y + u2* private_key*G.y):
        return False
    if (C.x != ( z*(s**(-1)) + r*private_key*(s**(-1)) ) * G.x) or (C.y != ( z*(s**(-1)) + r*private_key*(s**(-1)) ) * G.y):
        return False
    return True
    pass

# Ax ≡ B (MOD C)
def congru(a,b,c):
    for i in range(0,c):
       if ((a*i - b)%c)== 0 :
          return True
    return False

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

        s = int(generate_s(k, z, r, private_key, curve.n))
        r = int(r)
    return Point(r,s)

#def verify(message, signature, public_key, curve : Curve, private_key):
def verify(message, signature, public_key, curve : Curve):
    # message = int(message,base=16)
    sign = signature.split("-")
    s = int(sign[1])
    r = int(sign[0])
    print("r = ", r)
    print("s = ", s)
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
    s_pow_min1 = s**(-1) % curve.n
    print("spow min1 mod n = ", s_pow_min1%curve.n)
    print("z = ",z, "|", type(z))
    print("r = ",r, "|", type(r))
    print("s_pow_min1 = ", s_pow_min1, "|", type(s_pow_min1))
    print("curve.n = ", curve.n)
    u1 = (z * s_pow_min1)
    u2 = (r * s_pow_min1)
    # u1 = ((z * s_pow_min1) % curve.n)
    # u2 = ((r * s_pow_min1) % curve.n)
    # u1 = (z * s_pow_min1 % curve.n)
    # u2 = (r * s_pow_min1 % curve.n)

    print("public key =  ",public_key)
    Q = public_key.split("-")
    Q_x = int(Q[0])
    Q_y = int(Q[1])
    QA = Point(Q_x, Q_y)

    #Calculate the curve point (x1, y1) = u1 x G + u2 x Qa
    print("u1 = ",u1, "|", type(u1))
    print("G_x = ", curve.G_x,"|", type(curve.G_x))
    print("G_y = ", curve.G_y,"|", type(curve.G_y))
    print("u2 = ",u2, "|", type(u2))
    print("Q_x = ",Q_x,"|", type(Q_x))
    x1 = u1 * curve.G_x + u2 * Q_x
    y1 = u1 * curve.G_y + u2 * Q_y
    x1 = int(x1)
    y1 = int(y1)
    C = Point(x1, y1)
    # p1 = Point(u1 * curve.G_x, u1 * curve.G_y)
    # p2 = Point(u2 * curve.Q_x, u1 * curve.Q_y)

    # check r = x1 mod n
    print("x1 = ", x1)
    print(type(x1))
    #v = x1 % curve.n
    print("r = ", r)

    G = Point(curve.G_x, curve.G_y)
    #print(test(C, u1, G, u2, QA, private_key,z,r,s))
    return congru(r, C.x, curve.n)