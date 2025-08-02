user_num = input("Enter a number : ")

num_factorial = 1 

for i in range ( 1 , int(user_num) + 1  ) :
    num_factorial *= i 

print(num_factorial)

# while user_num > 0 :
#     num_factorial *= user_num
#     user_num -= 1

# print(num_factorial)