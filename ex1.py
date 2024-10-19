def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n in (0, 1):
        return 1
    else:
        return n * factorial(n - 1)

def process_list(numbers):
    # Check if all elements in the list are non-negative integers
    if not all(isinstance(x, int) and x >= 0 for x in numbers):
        raise ValueError("All elements in the list must be non-negative integers.")
    
    # Calculate the factorial for each number in the list
    result = [factorial(num) for num in numbers]
    return result

# Example usage of the process_list function
try:
    numbers_list = [0, 1, 3, 5, 7]
    factorials = process_list(numbers_list)
    print(f"Factorials of {numbers_list} are: {factorials}")
except ValueError as e:
    print(e)
