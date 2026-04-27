class Car:

     def __init__(self):
          print("我是无参方法init")
          self.color = "红色"
          self.number = 3

     def run(self):
          print(f"车的颜色是{self.color}，轮胎数量是{self.number}")


c1 = Car()
c1.color = "蓝色"
c1.number = 4
c1.run()
print("*"*20)
c2 = Car()
c2.run()
