if("2==2"):
    print("true")
    
    #syntax
    
    if("condition"):
        # statement1
        # statement2
        # statement3
        # statement4
        
        print("if block")
    else:
        print("else block")
        
#example 1

if(2-1 == 1):   # true
    a=2
    print(a)
    print("true")
elif(2 == 2): # false
    print("2 re")    
else:
    print("false")
    
if("t"=="t"):
    print("t")
    

marks = 72
if(marks > 80):
    print("read science")
    
elif(marks<70):
    print("read management")
    
else:
    print("reaad arts")


# two (and only) h/w ########################   //// camel case and  snake_case are different.
# camel case= "thisIsCamelCase"
# snake_case="this_is_snake_case"


# nested condition

# marks=90
# if (marks==90):
#     print("if block")
#     if(2==2):
#         print("2")
#     elif(3==4):
#         print("3 is equal to 4")
#     else:
#         print("fail")
        
        # else:
    #     print("empty block")
    
    
    
# on 4/4/2024
    
# marks=70
# if((marks>=65 and marks<=100) or (marks>=-1 and marks<65)):
#     print("pass")
# else:
#     print("fail")
        
#  grade--------------------->       
science=70
eng=62
math=89
social=65
nepali=55
t=500
s=science+eng+math+social+nepali
p=(t/s)*100
if(p>=80 ,99 and p<100):
        print("grade A")
elif(p>=60 ,79 and p<80):
        print("grade B")
elif(p>=40 ,69 and p<60):
        print("grade C")
elif(p>=20 ,39 and p<40):
        print("grade D")
else:
        print("fail")
    #     print("percentage",p,"%")
    # else:
    #     print("fail")
    
    
# percentage-------------------->>>
# def perc():
science==70
eng==62
math==89
social==65
nepali==55
t==500
s=science+eng+math+social+nepali
p=(s/t)*100
if(p>=40 and p<100):
    print("percentage is" ,p)
# elif(p>=60 and p<80):
#     print("percentage is" ,p)
# elif(p>=60 and p<80):
#     print("percentage is" ,p)
# elif(p>=60 and p<80):
#     print("percentage is" ,p)
else:
    print("Fail")
    
# one line if statement   ----------------------->
gender = "female"    
a = "female" if gender=="female" else "male"
print(a)