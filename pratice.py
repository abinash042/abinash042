

# print("Twinkle, twinkle, little, star,\n\thow Iwonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \ntwinke twinkle little star \n\thow i wonder what you are")


# import sys  # Import the sys module to access system-specific parameters and functions

# # Print the Python version to the console
# print("Python version")

# # Use the sys.version attribute to get the Python version and print it
# print(sys.version)

# # Print information about the Python version
# print("Version info.")

# # Use the sys.version_info attribute to get detailed version information and print it
# print(sys.version_info)

# import platform
# print(platform.python_version())


# # import date and time module
# print ("current date and time :")
# import datetime
# print (datetime.datetime.now())



# # Import the 'datetime' module to work with date and time
# import datetime

# # Get the current date and time
# now = datetime.datetime.now()

# # Create a datetime object representing the current date and time

# # Display a message indicating what is being printed
# print("Current date and time : ")

# # Print the current date and time in a specific format
# print(now.strftime("%Y/%m/%d %H:%M:%S"))

# # Use the 'strftime' method to format the datetime object as a string with the desired format

# radius = float(input("enter the radius of circle"))
# pi = 22/7
# Area = (f'{pi}*{radius^2}')
# print ("Area of circle is :",Area)


# from math import pi
# radius = float(input("enter the radius of circle: "))
# area =pi*radius**2
# print("Area of circle with radius " + str(radius) + " is: " + str(area))

# fname=input(" enter tour first name ")
# lname=input(" enter your last name ")

# print("my name is " + fname+ " " + lname)


# n=input("input some comma seperated numbers: ")
# list = n.split(",")
# tuples=tuple(list)
# print("list", list)
# print("tuples", tuples)

filename = input("enter the file name: ")
extent = filename.split(".")
print("the extension of file: .",extent[-1])

