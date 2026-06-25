# Question 1: Tuple Programs (a to l)

# a. Create a tuple with 5 different elements
my_tuple = ("Track A", "Track B", "Track C", "Track D", "Track E")
print("Original Tuple:", my_tuple)

# b. Access the first and last elements
print("\nFirst Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])

# c. Slice the tuple and print the middle 3 elements
print("\nMiddle 3 Elements:", my_tuple[1:4])

# d. Concatenate two tuples
tuple2 = ("Track F", "Track G")
new_tuple = my_tuple + tuple2
print("\nConcatenated Tuple:", new_tuple)

# e. Reverse a tuple using slicing
print("\nReversed Tuple:", my_tuple[::-1])

# f. Count how many times an element appears
count_tuple = ("Track A", "Track B", "Track A", "Track C", "Track A")
print("\nCount of 'Track A':", count_tuple.count("Track A"))

# g. Find the index of a specific element
print("\nIndex of 'Track C':", my_tuple.index("Track C"))

# h. Check if an element exists in a tuple
element = "Track D"
if element in my_tuple:
    print("\n", element, "exists in the tuple.")
else:
    print("\n", element, "does not exist in the tuple.")

# i. Convert a list to a tuple
my_list = ["Track X", "Track Y", "Track Z"]
tuple_from_list = tuple(my_list)
print("\nTuple from List:", tuple_from_list)

# j. Sort a tuple of numbers in ascending order
num_tuple = (45, 12, 89, 23, 7)
sorted_tuple = tuple(sorted(num_tuple))
print("\nSorted Tuple:", sorted_tuple)

# k. Repeat a tuple 3 times
print("\nRepeated Tuple:", my_tuple * 3)

# l. Check tuple immutability
try:
    my_tuple[0] = "Track Z"
except TypeError as e:
    print("\nTuple Immutability Test:", e)
