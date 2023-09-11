class Rectangle:
    width=None;
    height=None;
    def __init__(self,w, h):
        self.width = w;
        self.height=h;
    def set_width(self,w):
        self.width=w;
    def set_height(self,h):
        self.height=h
    def get_area(self):
        
        return self.height*self.width
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def get_picture(self):
        shape=""
        if(self.width>50 or self.height>50):
            return "Too big for picture."
        for i in range(self.height):
            for j in range(self.width):
                shape+="*"
            shape+='\n'
        return shape;    
    def get_amount_inside(self,shape): #check this one out!
        remainderArea=self.get_area()
        #print("Self area = ",remainderArea)
        #print("Passed shape area = ",shape.get_area())
        counter=0
        if(self.get_area()==shape.get_area()):
            return 0
        if(self.get_area()<shape.get_area()):
            return 0
        while(remainderArea>=0):
            remainderArea-=shape.get_area()
            counter+=1
        timesInside = (self.get_area()/shape.get_area())
        return counter
    def __str__(self):
        #Rectangle(width=10, height=3)
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"
  
''' 
set_width
set_height
get_area: Returns area (width * height)
get_perimeter: Returns perimeter (2 * width + 2 * height)
get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
get_picture: Returns a string that represents the shape using lines of "*".
The number of lines should be equal to the height and the number of "*" in each line should be equal to the width.
There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
get_amount_inside: Takes another shape (square or rectangle) as an argument.
Returns the number of times the passed in shape could fit inside the shape (with no rotations).
For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

'''
class Square(Rectangle):
    def __init__(self,sLength):
        self.height=sLength
        self.width=sLength
    def __str__(self):
       return "Square(side="+str(self.width)+")"
    
    def set_width(self,w):
        self.width=w;
        self.height=w
    def set_height(self,h):
        self.height=h
        self.width=h
    def set_side(self,s):
        self.height=s
        self.width=s


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_area())
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

#Test 2:

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

#test 3
rect.set_height(8)
rect.set_width(16)
#print(rect.get_amount_inside(sq))
print(rect.get_amount_inside(rect))

