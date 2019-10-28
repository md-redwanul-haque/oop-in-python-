class A:
    def display1(self):
        print( "hellow class A")
        
class B(A):
    def display2(self):
        print( "hellow class B")
class c(B):
    def display3(self):
        super().display1()
        super().display2()
        
        print( "hellow class C") 
        

        
p= A()
p.display1()
Q= B()
Q.display2()
r = c()
#r.display1()
#r.display2()
r.display3()