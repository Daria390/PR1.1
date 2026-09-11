def calculate_x(a, b):
    if a < b:
        x = (a * 3 - 5) / b
    elif a == b:
        x = -4
    else:
        x = (a**4 + b) / a
    return x