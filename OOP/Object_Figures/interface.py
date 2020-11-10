from figury import Rectangle, Cuboid

cuboid = Cuboid(Rectangle(2, 3), 4)
print(cuboid.count_surface_area())

def count_surface_area(self):
        return 2 * self.base.count_area() + 2 * self.base.edgeA * self.height + 2 * self.base.edgeB * self.height
