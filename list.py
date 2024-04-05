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


list in list
data=[1,2,3,4,['abiansh','kuamr']]
print(len(data))
print(data[-2][0])       #output abiansh
print(type(data[0]))
