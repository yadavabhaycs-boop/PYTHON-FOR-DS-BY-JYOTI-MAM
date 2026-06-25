# Question 2: List Programs (a to g)

# a. Find the largest number in a list
numbers = [12, 45, 7, 89, 23]
print("Largest Number:", max(numbers))

# b. Remove duplicates from a list
list1 = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(list1))
print("\nList after removing duplicates:", unique_list)

# c. Count how many even numbers are in a list
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
print("\nNumber of even elements:", count)

# d. Input 5 numbers and store them in a list
user_list = list(map(int, input("\nEnter 5 numbers separated by space: ").split()))
print("List:", user_list)

# e. Function to return the average of all numbers in a list
def average(lst):
    return sum(lst) / len(lst)

print("\nAverage:", average(numbers))

# f. Convert a string into a list of characters
text = "Python"
char_list = list(text)
print("\nList of Characters:", char_list)

# g. Join all elements of a list into a single string
words = ["Python", "is", "Easy"]
joined = " ".join(words)
print("\nJoined String:", joined)
