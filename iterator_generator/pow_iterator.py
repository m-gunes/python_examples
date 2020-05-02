class Pow:
    def __init__(self, max_val, init_val=1):
        self.max_val = max_val
        self.init_val = init_val

    def __iter__(self):
        return self

    def __next__(self):
        if self.init_val <= self.max_val:
            result = self.init_val ** 2
            self.init_val += 1
            return result
        else:
            raise StopIteration


pow = Pow(5)

for i in pow:
    print(i)

# print(next(pow))
# print(next(pow))
# print(next(pow))
# print(next(pow))
# print(next(pow))
# print(next(pow))
