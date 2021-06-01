#Problem 2
#Fill in the class

class Cylinder():
    
    def __init__(self,height=1,radius=1):
      self.height = height
      self.radius = radius
        
    def volume(self):
        return 3.14*(self.radius**2)*self.height

    def surface_area(self):
        return (2*3.14*(self.radius)*self.height) + 2*(3.14*(self.radius)**2)

cylind=Cylinder(2,3)
print('This is volume',cylind.volume())
print('This is surface area',cylind.surface_area())
