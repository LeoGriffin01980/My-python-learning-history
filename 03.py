class Car:
     def __init__(self,color,number):
          self.color = color
          self.number = number
     def run(self):
          print(f"车的颜色是{self.color}，轮胎数量是{self.number}")
    
c1 = Car("红色",3)
c1.run()
print("-"*23)
c2 = Car("蓝色",4)
c2.run()
