# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:
# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("Pick a number, any number: "))

if num % 4 == 0:
  print(str(num), "is divisible by 4!")
elif num % 2 == 0:
  print(str(num), "is an even number.")
else:
  print(str(num), "is an odd number.")

# Extra #2

# divisor = int(input("Please enter the divisor: "))
# dividend = int(input("Please enter the dividend: "))

# if dividend % divisor == 0:
#   print(str(divisor), "evenly divides", str(dividend) + ".")
# else:
#   print(str(divisor) + " does not evenly divide " + str(dividend) + ".")
