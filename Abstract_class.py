from abc import ABC,abstractmethod


class A(ABC):
    def area(self):
        print("hellow")
    @abstractmethod
    def new(self):
        pass
        
        
class B:
    def shape(self):
        print("hei ")
    def new(self):
        print("hellow anik")
        

#K=A()     #you cant't create method when it is an abstract class
#K.area()        
d= B()
d.new()
        
        
