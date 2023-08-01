# add your code here

# Define FizzBuzz
def FizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# Define the range of numbers to iterate through
for num in range(1, 101):
    # Call the FizzBuzz function to print the appropriate word or number
    FizzBuzz(num)
