def http_error(status):
    match status:
        case 400:
            return "bad request"
        case 404:
            return "not found"
        case 418:
            return "I'm a teapot"
        case _:
            raise ValueError("Not a point")
        