#Task 1
# Write a Python program to count the number of characters (character frequency) in a string.
name = "Omar muhammad"
print(name)
print("count (a): " , name.count("a"))
count_a = name.count("a")

start_index = 0
for i in range(count_a):
    index_a = name.index("a", start_index)
    print(f"index {i+1}: {index_a}")
    start_index = index_a + 1

