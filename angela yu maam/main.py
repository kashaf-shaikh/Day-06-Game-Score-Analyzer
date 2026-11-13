# def greet_user(name):
#     print(f"Welcome {name}!  Welcome to Python.")
#
# greet_user("Kashaf")
# def add_numbers(num1,num2):
#     add = num1 + num2
#     return add
#
# result = add_numbers(5,5)
# print(f"The sum is : {result}")

# 📝 Next Challenge — Function + Conditions
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "odd"

user_number = int(input("Enter number you want to check whether it's even or odd :\n"))
result = check_even_odd(user_number)
print(f"{user_number} is {result}")

