import tracemalloc
import time


def max_time(limit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()

            result = func(*args, **kwargs)

            end = time.time()
            if end - start > limit:
                print("Function took too long!")

            return result

        return wrapper
    return decorator


def memory_usage(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        result = func(*args, **kwargs)

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"Memory peak: {peak / 1024:.2f} KB")
        return result

    return wrapper


@max_time(1)
@memory_usage
def func_ex(number=10000000):
    for i in range(number):
        i += 1
    print("cool")


func_ex()
