# a={
#     "name":"sudan",               #key is always in small letter
#     "address":1245,             #value can be any data type
#     "population":3000000       #data about population of sudan 
#     "nested_dict":{            #a nested dictionary
# }                                #country name should match the key 
# print(a["name"])                #how to access value using key




# print(a["population"])         #accessing nested values
# cities=a["city name"]                   #accessing all information related to cities
# print(cities.keys())            #show all available keys for cities
# print(cities.values())          #show all available values for cities (coordinates)
# #to get specific coordinate of a city:
# print(cities["New City"].values())     #for example New City's coordinate

# #accessing the value by its key  
# print(a["name"])                #output: sudan  


# # a['name']='sudan_abdalla'      #changing the value of 'name' to 'sudan_abdalla'
# print(a)                        #output: {'name': 'sudan_abdalla', 'address': 1245, 'population': 3000000}




# #check if a specific key exists or not  
# if "capital" in a :            #this will return True because there is no such key as capital  in our dictionary. 
# if "name" in a :               #True  
#     print("yes") 
# else:                          #False    
#     print("no")       

# #add new key-value pair to dictionary    
# a["area"]=986756.0             #adding area information to country details

# #update existing key's value          
# a["population"]=4000000      #updating population information of sudan

# #remove a particular key from dictionary                   
# del a["area"]                  #removing area information from country details

# #get all keys present in the dictionary           
# print(list(a.keys()))         #['name', 'address', 'population']

# #get all values present in the dictionary
# print(list(a.values()))             #[u'sudan', 1245, 4000000]

# #get a list of tuples containing key-value pairs
# print(list(a.items()))               [('name', u'sudan'), ('address', 1245), ('population', 4000000)]
# }

# print(a["name"]) # sudan


b = {"sports":"cricket","player":"paras khadka"}
a ["nested_dict"] = b                                         # adding nested dictionary to main dictionary
print(a)                                                       #

# # print(len(a))
# print(a['nested_dict']['player'])     



