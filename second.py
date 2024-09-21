






def handle_input(value):
    match value:
        case int():
            return f"Got an integer: {value}"
        case str():
            return f"Got a string: {value}"
        case list():
            return f"Got a list with {len(value)} elements"
        case _:
            return "Got something else"

# Testing the function
print(handle_input(42))        # Output: Got an integer: 42
print(handle_input("hello"))   # Output: Got a string: hello
print(handle_input([1, 2, 3])) # Output: Got a list with 3 elements
print(handle_input(3.14))      # Output: Got something else