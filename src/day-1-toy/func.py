# Write a function is_even that will return true if the passed in number is even.
# def is_even(num):
#     return num%2 == 0

is_even = lambda num: num%2 == 0

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
print("Even") if is_even(int(num)) else print("Odd")