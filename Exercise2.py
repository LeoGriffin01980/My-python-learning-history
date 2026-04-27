class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def get_area(self):
        print(f"面积是{self.width*self.height}")    
    def get_perimeter(self):
        print(f"周长是{2*(self.width+self.height)}")

demo1 = Rectangle(10,20)
demo1.get_area()
demo1.get_perimeter()   