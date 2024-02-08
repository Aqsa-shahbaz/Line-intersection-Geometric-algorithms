class Points :
    def __init__ (self):
        self.x = None
        self.y = None
    
    def set_point(self,x,y):
        self.x = x
        self.y = y

    def ccw(self, p1, p2, p3):
        val = ((p3.y - p2.y) * (p2.x - p1.x)) - ((p2.y - p1.y) * (p3.x - p2.x))
        if val == 0: #if points are collinear
            return 0
        elif val > 0: # if points are in counter-clockwise orientation
            return 1
        else:
            return -1 # if points are in clockwise orientation

class Lines :
    def __init__(self):
        self.p1 =Points()
        self.p2 =Points()
        self.p3 =Points()
        self.p4 =Points()
        self.p =Points()

    def check_points(self):
        
        test1 = self.p.ccw(self.p1, self.p2, self.p3) * self.p.ccw(self.p1, self.p2, self.p4)
        test2 = self.p.ccw(self.p3, self.p4, self.p1) * self.p.ccw(self.p3, self.p4, self.p2)
        return (test1 <= 0) and (test2 <= 0)
# Returns:
    # True if line segments intersect or touch
    # False if line segments do not intersect