# import random

# n = random.randint(1,15)
# tries =1 

# while tries <= 5:
#     guess = int(input("Guess the number: "))
#     if guess < n:
#         print("Too low")
#     elif guess > n:
#         print("Too high")
#     else:
#         print("You guessed it in", tries, "tries")
#         breaks

#     tries = tries + 1

# if not guess == n:
#     print("You have run out of tries")
#     print("The number was", n)
    
    
import random

random_number = random.randint(1,15)
print(random_number)
tries = tries+1
number = int(input("enter a number"))
while(number!=random_number):
    print(f'{number} is wrong guess')
    number = int(input("wnter a number again: "))
    
print(f'weldone {number} is correct guess, you guess is{tries+1}')
    
    
    