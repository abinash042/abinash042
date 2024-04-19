# def showdata():
#     print("welcome to my home")
    
# showdata()




# # def print_number(n,a):
# #     if n == 0:
# #         return

# #     print_number(n-1,a)
# #     print(a[n-1],end=" welcome to my course ")
# #     print_number()



# # user define function with argument and return type

# def add(a,b):
#     print(a+b)

# add(10,20)
# add(60,40)

# # default parameter function 

# def add(a,b=10):
#     print(a+b)

# add(10)
# add(10,20)


# # return values from function

# def add(a,b):
#     return a+b

# print(add(10,20))

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x-1)
    
# num = 5
# print("this factorial of", num, "is", factorial(num))

# print(random.randint(0,3))


def recursive_fibo(n):
    if n<= 1:
        return n
    else:
        return recursive_fibo(n-1) + recursive_fibo(n-2)


n_terms = 10