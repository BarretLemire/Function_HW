def add(x: float, y: float) -> float:
    result = x + y
    return result

def square(x: float) -> float:
    result = (x * x)
    return result

def multiply(x: float, y: float) -> float:
    result = x * y
    return result

def add_squares(x: float, y: float) -> float:
    x_squared = square(x)
    y_squared = square(y)
    result = add(x_squared, y_squared)
    return result


(add_squares(1.8, 2.3))