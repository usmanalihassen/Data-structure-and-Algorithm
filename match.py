def point_location(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"On the X-axis at {x}"
        case (0, y):
            return f"On the Y-axis at {y}"
        case (x, y):
            return f"At coordinates ({x}, {y})"
        case _:
            return "Unknown location"
def function():
    print("hello")
    print("my name is osman")
function()
def add(x,y):
    print(x+y)

add(2,4)
def sum(x,y):
    c=x+y
    print(f"the sum is {c}")
sum(100,200)