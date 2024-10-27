squares=[]
for i in  range(10):
    squares.append(i**2)
print(squares)
squares_of_even = [x**2 for x in range(10) if x % 2 == 0]
print(squares_of_even)


