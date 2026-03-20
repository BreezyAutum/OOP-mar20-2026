"""
Create a class that has:
• Attributes: width and length
• Constructor to initialize length and width
• Getters and setters for the attributes
• 2 methods for calculating the area and perimeter of the rectangle.
"""
class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width
  def get_length(self):
    return self.length
  def get_width(self):
    return self.width
  def set_length_and_width(self, new_length, new_width):
    self.length = new_length
    self.width = new_width
  def calc_area(self):
    return self.length * self.width
  def calc_perimeter(self):
     return 2 * (self.length + self.width)
length = int(input("Enter the length of a rectangle.\n"))
width = int(input("Enter the width of a rectangle.\n"))
rect = Rectangle(length, width)
rect_area = rect.calc_area()
rect_perimeter = rect.calc_perimeter()
print(rect_area, "\n", rect_perimeter)