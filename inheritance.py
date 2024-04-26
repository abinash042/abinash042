class Dad():
    a = "test"
    
class Son(Dad):
    b = "hello"
    
obj = Son()

print(obj.b)
print(obj.a)

class Parent():
    a =10
    b =13
    
    def add(self):
        return self.a + self.b
class Child():
    
    def sub(self):
        return self.a - self.b
    
    def calc(self):
        return self.add(), self.sub()
    
obj = Child()
print(obj.calc())

class Parent():
    def __init__(self):
        self.a = 10
        self.b = 11
        
    def add(self):
        return self.a
    
class Child(Parent):
    def __init__(self):
        self.c = 9
        self.d = 11
        
    def sub(self):
        return self.add()
    
obj = Child()
print(obj.sub())
    
    


