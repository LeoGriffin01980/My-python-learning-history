class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"我是{self.name}，我今年{self.age}岁")

    def bark(self):
        print(f"{self.name}is barking")

dog1 = dog("leo",10)
dog1.bark()
