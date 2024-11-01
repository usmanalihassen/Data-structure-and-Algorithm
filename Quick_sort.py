def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)
#EXERCISE-3
def quick_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the pivot (we're using the last element here)
    pivot = arr[-1]
    left = []  # Elements less than pivot
    right = []  # Elements greater than pivot
    
    # Partitioning step
    for i in range(len(arr) - 1):  # Exclude the pivot itself
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    # Recursively sort left and right partitions, then combine
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

        