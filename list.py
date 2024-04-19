# a = []  #empty list

# a=[1,2,3,4,5,6]

# a = ['broadway' ,1,2,3]
# print(a)



b=['a','b','c','d','e','f','g','h','i','j']   #list with one string element
print(b[0],b[3])

# index length
print(len(b))    #length of the list



# slicing 
print(b[:3])     #from beginning to third element
print(b[3:7])     #from fourth to seventh element
print(b[-1])      #last element in the list
print(b[-3:-1])     #third last and second last elements


# list in list
# data=[1,2,3,4,['abiansh','kuamr']]
# print(len(data))
# print(data[-2][0])       #output abiansh
# print(type(data[0]))

teachers=['rahul', 'sonya', 'nasir' ,'irfan', 'haris', [1,2,3]]
teachers.append('sudan')
teachers.append(1)

teachers.insert(-1, 'pink')         #return the position of the first occurrence of an item
                          #if not found then it will return error
print(teachers)

teachers.extend(["python", "java"])        #add multiple items at once
print(teachers)


del teachers[0]            #deletes the first element from the list
print(teachers)

teachers.remove("python")
print("after removing python : ",teachers)

teachers.pop(0)             #removes the specified item using its value
                              #it returns the removed item
print(teachers.pop())               #returns and removes the last item
# try:
#     teachers.remove("php")           # if the given value is not present in the list then it will show a ValueError
#     teachers.remove("C++")             # if C++ is not present in the list then it gives a ValueError
# except ValueError as e:
#     print("Value Error: ",e)
