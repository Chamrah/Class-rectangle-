class Rectangle():
# Parametric
    def __init__(self,length,width):
        self.length = length
        self.width = width

# # Default parametre
#     def __init__(self):
#         self.length = 1
#         self.width = 2

# # Parametre by copy
#     def __init__(self,oldR):
#         self.length = oldR.length
#         self.width = oldR.width
    
# function perimeter and area and issquare and display rectangle
    def perimeter(self):
        p = (self.length + self.width) * 2
        return p
    
    def area(self):
        a = self.length * self.width
        return a
    
    def issquare(self):
        if (self.length == self.width) :
            return True
        else:
            return False
    
# Displaying the length and width of the rectangle
    def display_rectangle(self):
        print("The length {} and width {} and the perimeter {} and the area of the rectangle".format(self.length, self.width, self.perimeter(), self.area(), self.issquare()))