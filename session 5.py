name = input("what is your name? ")
age = input("what is your age? ")
# print("Hello", ", name, "!", sep="")

try:
age = int(age) #convert string to integer
birth_year = 2024 - age
print(name, ", you were born in ", birth_year, ".", sep="")
number = input("give me a number to divide the age ")
number = int(number)
print(age/number)

except ValueError:
    print("Invalid age. Please enter a number. ")
except ZeroDivisionError
    print("you cannot divide by zero")
    else
    print("no exceptions were raised")
    finally
    print("thankyou for playing")

print("we will play a drinking game")

try
        name