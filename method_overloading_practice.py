class shape:
    def __init__(self, base , height ):
        self.base = base 
        self.height= height 
    def area(self):
        print("hlw Md anik ")
        
class triangle(shape):
    def area(self):
        super().area() # for show previous area method
        
        value = 0.5 * self.base * self.height
        print("Area value  :",value)
        
        
A=triangle(10,20)
A.area()

        

