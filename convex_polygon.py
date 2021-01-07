import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def get_coor(self):
        return (self.x, self.y)
    
class Edge:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def length(self):
        return math.sqrt((self.p1.x - self.p2.x)**2 + (self.p1.y - self.p2.y)**2)
    
class Angle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.e12 = Edge(p1, p2)
        self.e23 = Edge(p2, p3)
        self.e13 = Edge(p1, p3)
        
    def cos(self):
        a = self.e12.length()
        b = self.e23.length()
        c = self.e13.length()
        return (a**2 + b**2 - c**2) / (2 * a * b)
    
def convex_polygon(df, x_col, y_col):   
    l_convex = []
    p1 = Point(df.iloc[0][x_col], df.iloc[0][y_col])
    p2 = Point(df.iloc[1][x_col], df.iloc[1][y_col])
    while True:
        min_cos = 1
        for values in df[[x_col, y_col]].values:
            if (values[0] not in [p1.x, p2.x]) & (values[1] not in [p1.y, p2.y]):
                p_tmp = Point(values[0], values[1])
                angle = Angle(p1, p2, p_tmp)
                if angle.cos() < min_cos:
                    min_cos = angle.cos()
                    p3 = p_tmp

        if p3.get_coor() in l_convex:
            l_convex.append(p3.get_coor())
            break
        else:
            p1 = p2
            p2 = p3
            l_convex.append(p3.get_coor())
            
    index = l_convex.index(l_convex[-1])
    return l_convex[index:]
