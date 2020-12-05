from util import modinv

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def is_netral(self):
        return self.x is None and self.y is None
    
    def inverse(self):
        if(self.x == None):
            return Point(None, -self.y)
        elif(self.y == None):
            return Point(self.x, None)

        return Point(self.x, -self.y)
    
class Curve():
    def __init__(self, a, b, p, G_x, G_y, n):
        self.a = a
        self.b = b
        self.p = p
        self.G_x = G_x
        self.G_y = G_y
        self.n = n

        self.generate_field()
    
    def netral_result(self):
        return Point(None, None)
    
    def add_point(self, p1, p2):
        if(p1.is_netral()):
            return p2
        elif(p2.is_netral()):
            return p1
        elif p1.y == -p2.y :
            return netral_result()
        elif (p1.x == p2.x) and (p1.y == p2.y) and (p1.x == 0):
            return netral_result()
        else:
            m = (p2.y - p1.y) / (p2.x - p1.x)
            xr = m*m - p2.x - p1.x
            yr = m * (p2.x - xr) - p2.y

            return Point(xr, yr)
    
    def next_point(self, p1) :
        return p1.inverse()

    def add_point_gf(self, p1, p2):
        if(p1.is_netral()):
            return p2
        elif(p2.is_netral()):
            return p1
        elif p1.y == -p2.y :
            return netral_result()
        elif ((p1.x == p2.x) and (p1.y == p2.y) and (p1.x == 0)):
            return netral_result()
        else:
            m = (p2.y - p1.y) * modinv((p2.x - p1.x), self.p)
            xr = (m*m - p2.x - p1.x) % self.p
            yr = (m * (p2.x - xr) - p2.y) % self.p

            return Point(xr, yr)
    
    def subtract_point_gf(self, p1, p2):
        p2_new = p2.inverse()
        return add_point_gf(p1, p2_new)

    def generate_field(self):
        # y^2 = x^3 + ax + b mod p in x = |0, p-1|
        for x in range(self.p - 1):
            y2 = x * x * x + self.a * x + self.b
            y2 = y2 % self.p

            counter = 0
            y_pos = 0
            while((y_pos < self.p-1) and (counter == 0)) :
                if((y_pos * y_pos) % self.p == y2) :
                    counter += 1
                    self.G_x = x
                    self.G_y = y_pos
                else:
                    y_pos += 1

def demo_curve():
    return Curve(a=0,b=7,p=11,G_x=None,G_y=None,n=500)