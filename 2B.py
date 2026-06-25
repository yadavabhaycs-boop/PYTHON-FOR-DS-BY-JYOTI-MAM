# Original nested tuple of tracks
track_tuple = (
    ("Track A", 20),
    ("Track B", 21),
    ("Track C", 22)
)

# Sorting the nested tuple by track code (index 1)
sorted_tracks = sorted(track_tuple, key=lambda x: x[1])

# Display the sorted result
print("Sorted Tracks (by track code):", sorted_tracks)
