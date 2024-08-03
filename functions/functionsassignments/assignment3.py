def count_calls_decorator(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Function {func.__name__} has been called {wrapper.call_count} times")
        return func(*args, **kwargs)

    wrapper.call_count = 0  # Initialize the call count

    return wrapper

# Applying the decorator to a function
@count_calls_decorator
def example_function():
    print("Inside the example function")

# Calling the decorated function multiple times
example_function()
example_function()
example_function()
