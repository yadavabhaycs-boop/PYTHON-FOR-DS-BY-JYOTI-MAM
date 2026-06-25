#S123 ABHAY YADAV

# 1. Create nested tuple with tracks
track1 = ("Track A", 20)
track2 = ("Track B", 21)
track3 = ("Track C", 22)

track_tuple = (track1, track2, track3)
print("Nested Tuple:", track_tuple)

# 2. Indexing
print("First track tuple:", track_tuple[0])
print("Name of second track:", track_tuple[1][0])

# 3. Negative indexing
print("Last track tuple (negative index):", track_tuple[-1])
print("Name of last track:", track_tuple[-1][0])

# 4. Loop through the nested tuple
print("\nAll Tracks:")
for track in track_tuple:
    print(f"Track Name: {track[0]}, Code: {track[1]}")

# 5. Reverse the tuple
reversed_tuple = track_tuple[::-1]
print("\nReversed Tuple:", reversed_tuple)

# 6. Slice the tuple (first two tracks)
sliced_tuple = track_tuple[0:2]
print("Sliced Tuple (first two tracks):", sliced_tuple)

# 7. Concatenate another track tuple
track4 = ("Track D", 23)
updated_tuple = track_tuple + (track4,)
print("After Concatenation:", updated_tuple)

# 8. Demonstrate immutability
try:
    track_tuple[0][1] = 999  # Trying to change track code
except TypeError as e:
    print("\nTuple Immutability Test: Error occurred ->", e) 
