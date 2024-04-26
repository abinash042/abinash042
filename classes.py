# # class Test():
# #     x =5
# # obj=Test()
# # print(obj.x)

# # use return

# class Test2():
#     x = 10
#     def testing_world(rahul):
#         print(rahul.x)
#         b ='this is tessting'(rahul.x)'world'
#         return b
#         # print(f'this is {rahul.x} testing world')
        
    
# obj2=Test2()
# print(obj2.testing_world())

class Test():
    x=1234
    b=1234
    def testing_world(self):
        print(self.x)
        b = "this is testing world"
        return b

obj=Test()
print(obj.testing_world())

