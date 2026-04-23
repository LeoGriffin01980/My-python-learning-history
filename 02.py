class Car:
    def run(self):
        print(f"{self}这个车在跑")
        

    def work(self):
        print(f"{self}这个车在工作")
        self.run()
        
        

c1 = Car()
c1.run()

c2 = Car()
c2.run()

c3 = Car()
c3.work()