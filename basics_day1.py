n=int(input(print("Enter the number")))
for i in range(2,n):
    if n % i ==0:
        print(False)
        exit()
print(True)

#swap using third variable
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

temp = num1

num1 = num2
num2 = temp

print("After swapping:")
print("The first number is:", num1)
print("The second number is:", num2)

#swap without third variable
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

x = x + y  # x becomes 15 (10 + 5)
y = x - y  # y becomes 5 (15 - 5)
x = x - y  # x becomes 10 (15 - 5)

print("After swapping:")
print("x =", x)  # Output: x = 10
print("y =", y)  # Output: y = 5

#palindrome
def is_palindrome(num):
  """Checks if a number is a palindrome (reads the same backward as forward).

  Args:
      num: The number to check.

  Returns:
      True if the number is a palindrome, False otherwise.
  """

  if num < 0:
    return False  # Negative numbers cannot be palindromes

  original_num = num
  reversed_num = 0
  while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

  return original_num == reversed_num

# Example usage
number = int(input("Enter the number:\n"))
if is_palindrome(number):
  print(number, "is a palindrome")
else:
  print(number, "is not a palindrome")
