import time


def calc_time(func):
    def wrapper(numbers):
        start_date = time.time()

        result = func(numbers)

        end_date = time.time()
        print(func.__name__ + " " + str(end_date - start_date) + " saniye sürdü.")

        return result

    return wrapper


@calc_time
def calculate_square(numbers):
    result = []
    for i in numbers:
        result.append(i ** 2)

    return result


@calc_time
def calculate_cube(numbers):
    result = []
    for i in numbers:
        result.append(i ** 3)

    return result


calculate_square(range(100000))
calculate_cube(range(100000))