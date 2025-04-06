import time

def time_consumption(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Funkcja {func.__name__} zajela {end_time - start_time:.4f} sekund")
        return result
    return wrapper

def log_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper