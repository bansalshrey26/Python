import math

class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    
    def area(self):
        self.area=self.length*self.breadth
        print("Area is: ",self.area)
        
    def perimeter(self):
        self.perimeter=2*(self.length+self.breadth)
        print("Perimeter is; ",self.perimeter)
        
    def cost_fencing(self,c):
        self.costt=c
        self.peri=2*(self.length+self.breadth)
        self.cost=self.peri*self.costt
        print("Cost of fencing is: ",self.cost)
        
    def cost_flooring(self,c):
        self.floor=c
        self.ar=self.length*self.breadth
        self.costfloor=self.floor*self.ar
        print("Cost of flooring is: ",self.costfloor)
        
    def sq(self):
        if self.length==self.breadth:
            print("It is a Square")
        else:
            print("It is a Rectangle")
    
    def diagonal(self):
        self.dia=math.sqrt(self.length**2+self.breadth**2)
        print("Length of diagonal is: ",self.dia)
        
R=[]
n=int(input("Enter Number of Rectangles: "))
for i in range(n):
    print("Value for Rectangle",i+1)
    x=int(input("Enter Length: "))
    y=int(input("Enter Breadth: "))
    R.append(rectangle(x,y))

ch='y'
while ch=='y':
    
    print("--------Menu--------")
    print("1. Area \n2. Perimeter \n3. Cost of Fencing \n4. Cost of Flooring \n5. Check for a Square \n6. Length of diagonal")
    z=int(input("Enter Choice: "))
    b=int(input("Enter Rectangle Number: "))

    R1=R[b-1]

    if b>=1 and b<=n:
        
        if z==1:
            R1.area()
        elif z==2:
            R1.perimeter()
        elif z==3:
            c=int(input("Enter Cost: "))
            R1.cost_fencing(c)
        elif z==4:
            c=int(input("Enter Cost: "))
            R1.cost_flooring(c)
        elif z==5:
            R1.sq()
        elif z==6:
            R1.diagonal()
        else:
            print("Invalid Input")
            
    ch=input("Do you want to continue (y/n)")
    if ch=='n':
        ch='n'
        print("Program Ended :) ")
    
        