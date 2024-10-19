def factorial(n):
    # Check if the input is valid
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Base case: 0! and 1! are both 1
    if n in (0, 1):
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

# Example usage of the factorial function
try:
    num = 5
    print(f"The factorial of {num} is: {factorial(num)}")
except ValueError as e:
    print(e)
