import math

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vector = [x, y, z]

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)
    
    def __getitem__(self, i):
        return self.vector[i]
    
    def __setitem__(self, i, value):
        self.e[i] = value

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
    
    def __rmul__(self, other):
        return Vector3(other * self.x, other * self.y, other * self.z)
    
    def __truediv__(self, other):
        return Vector3(self.x / other, self.y / other, self.z / other)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

        return self
    
    def __imul__(self, other):
        self.x *= other
        self.y *= other
        self.z *= other

        return self
    
    def __itruediv__(self, other):
        self.x /= other
        self.y /= other
        self.z /= other

        return self
    
    def length(self):
        return math.sqrt(self.length_squared())
    
    def length_squared(self):
        return self.x * self.x + self.y * self.y + self.z * self.z
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return Vector3(self.y * other.z - self.z * other.y,
                       self.z * other.x - self.x * other.z,
                       self.x * other.y - self.y * other.x)
    
    def unit_vector(self):
        return self / self.length()
    
    def __str__(self):
        return f"{self.x} {self.y} {self.z}"
    
    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __ne__(self, other):
        return not self == other
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))
    
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

Point = Vector3