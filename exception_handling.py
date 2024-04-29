a = 10
# print(a+b)

try:
    print(a+b)
except NameError as e:
    print(e)
except TypeError as e:
    print(e)
except SystemError as e:
    print(e)
except:
    print("error occured")