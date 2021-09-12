import math
class circle_compute():
	def __init__(self,my_radius):
		self.radius=my_radius
	def area_calculate(self):
		return math.pi*(self.radius**2)
	def perimeter_calculate(self):
		return 2*math.pi*self.radius
my_result = int(input("Enter the radius of circle..."))
circle = circle_compute(my_result)
print("The radius entered is :")
print(my_result)
print("The computed area of circle is ")
print(round(circle.area_calculate(),2))
print("The computed perimeter of circle is :")
print(round(circle.perimeter_calculate(),2))