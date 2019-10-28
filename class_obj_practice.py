class triangle:
    
     def __init__(self,base,height):
         self.base=base
         self.height=height
         
     def calculation(self):
         area= 0.5 * self.base * self.height
         print("Area = ",area)
     
     
         
first= triangle(10,20)
first.calculation()

second= triangle(20,30)
second.calculation()