def func():
    try:
        0/0
    except ZeroDivisionError:
        return 3
    return 5

print(func())