class Student:
    def run(self):
        print("学生在睡觉")

    def sleep(self):
        print(f"{self.color}的学生在睡觉，年龄是{self.age}")    
      
stu = Student()


stu.color = "red"
stu.age = 18

stu.sleep()

   