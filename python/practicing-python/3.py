# Take a list, say for example this one:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# and write a program that prints out all the elements of the list that are less than 5.

# Extras:
# 1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for num in nums:
  if num < 5:
    print(num)

# Extra #1

def filter_less_than(nums, upper_bound):
  return list(filter(lambda num: num < upper_bound, nums))

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
filtered_nums = filter_less_than(nums, 5)

print(filtered_nums)

# Extra #2

print(list(filter(lambda num: num < 5, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])))

# Extra #3

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def filter_less_than(nums, upper_bound):
  return list(filter(lambda num: num < upper_bound, nums))

upper_bound = int(input("Please enter an upper bound: "))

print(filter_less_than(nums, upper_bound))