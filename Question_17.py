""" 
17. Write a function that takes a list of numbers as input and returns a new list containing only the even numbers from the input list. Use list comprehension to solve this problem.

Example:

Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Output: [2, 4, 6, 8, 10]
"""

def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


list1=[1,2,3,4,5,6,7,8,9,10]
list2=get_even_numbers(list1)

print(list2)