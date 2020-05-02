
class Series:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

            # result = self.current
            # self.current += 1
            # return result


n_list = Series(1, 5)
print(list(n_list))

print('________________')

def series_generator(low, high):
    while low <= high:
        yield low
        low += 1


for i in series_generator(1,10):
    print(i)