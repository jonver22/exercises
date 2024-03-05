class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y =y

    def __add__(self, other):
        if isinstance(other, Vector):
            return vector(self.x + other.x, self.y + other.y)
        else:
            ValueError("error")

    def __str__(self):
        return f"vector({self.x}, {self.y})"

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y =y
        self.z =z

    def __add__(self, other):
            return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

vector1 = Vector(1,2)
vector1 = Vector(4,1)

p1 = Point3D(1,2,3)
p2 = Point3D(3,2,1)

result = vector1 + p1
print(result)
