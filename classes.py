# # Class and Object in python 
# #  class is a blueprint for creating object
# #  creating class
 
# class Student():
#      name = "Karan Kumar"
     
     
# # creating object (instance)

# s1 = Student()
# print(s1.name)


# class Car():
#     color = "blue"
#     brand ="mercedes"
    
# car1 = Car()
# print(car1.color)
# print(car1.brand)



# # # class Test():
# # #     x =5
# # # obj=Test()
# # # print(obj.x)

# # # use return

# # class Test2():
# #     x = 10
# #     def testing_world(rahul):
# #         print(rahul.x)
# #         b ='this is tessting'(rahul.x)'world'
# #         return b
# #         # print(f'this is {rahul.x} testing world')
        
    
# # obj2=Test2()
# # print(obj2.testing_world())

# class Test():
#     x=1234
#     b=1234
#     def testing_world(self):
#         print(self.x)
#         b = "this is testing world"
#         return b

# obj=Test()
# print(obj.testing_world())



# class Student():
    
#     def __init__(self, fullname):
#         self.name = fullname
#         print("adding new student in database...")
        
# s1 = Student("rahul")
# print(s1.name)

# s2 = Student("rohit")
# print(s2.name )
        
        
# class Sytudent():
#     college_name = "ABC College"
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     def welcome(self):
#         print("welcome student,", self.name)
        
#     def get_marks(self):
#         return self.marks
    
# s1 = Student("karan", 98)
# s1.welcome()
# print(s1.get_marks())



class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks =marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your average score is:", sum/3)
        
s1 = Student("thanos", [99,10,99])
s1.get_avg()
# print(s1.get_avg())
        





