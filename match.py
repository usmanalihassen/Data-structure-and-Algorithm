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
