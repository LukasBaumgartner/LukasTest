number = input("Enter a number: ")
try:
    number = int(number)
    if number % 3 == 0:
        print("This number is divisible by 3")
    else:
        print("This number is not divisible by 3")
except ValueError:
    print("This is not a valid number")

# [] - you got this wrong
# s[1::2] means:
# Start at index 1
# Go to end
# Step 2

s= "hello"
print(s[1:3:2])
# 3 is not included so produces e

help(type(7+3))