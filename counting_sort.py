# Input array
arr = [4, 2, 2, 8, 3, 3, 1]

# Step 1: Find the maximum value in the input array
max_value = max(arr)

# Step 2: Create a count array initialized to zero
count = [0] * (max_value + 1)

# Step 3: Count the occurrences of each element
for num in arr:
    count[num] += 1

# Step 4: Modify the count array to store the cumulative counts
for i in range(1, len(count)):
    count[i] += count[i - 1]

# Step 5: Create an output array
output = [0] * len(arr)

# Step 6: Build the output array using the count array
for num in reversed(arr):  # Traverse the input array in reverse for stability
    output[count[num] - 1] = num
    count[num] -= 1

# Output array is sorted
print("Sorted array:", output)
