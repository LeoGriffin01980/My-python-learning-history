class Car:
    def run(self):
         print("车在跑")
         print(f"我是run函数self的值是:{self}")

#c1.run()
c1 = Car()
print(f"对象:{c1}")
print(f"对象:(c1)的地址是:{id(c1)}")
c1.run()

#c2.run()
c2 = Car()
print(f"对象:{c2}")
print(f"对象:(c2)的地址是:{id(c2)}")
c2.run()

