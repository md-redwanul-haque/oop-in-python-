class atm:
    def customer(self):
        print("hellow dear customer ")
        
    def manager(self):
        print("hellow dear manager ")
    
    def author(self):
        print("Hellow Author saheb")
        
        
class user(atm):
    
    def permanent(self):
         print("hellow dear customer ")
         
    def temporary(self):
         print("hellow dear customer ")
         

A=atm()
A.author()
A.customer()
A.manager()
B=user()
B.author()
B.customer()
B.manager()
B.permanent()
B.temporary()