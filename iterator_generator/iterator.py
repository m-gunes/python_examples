class Kuvvet3:
    def __init__(self, max):
        self.max = max
        self.kuvvet = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.kuvvet <= self.max:
            result = 3 ** self.kuvvet

            self.kuvvet += 1

            return result
        else:
            # self.kuvvet = 0
            raise StopIteration


kuvvet = Kuvvet3(6)

for i in kuvvet:
    print(i)

# asagidaki dongu calismaz cunku else durumuna giriyor ve StopIteration firlatiyor
# eger else durumuna self.kuvvet = 0 yazarsak calisir
for j in kuvvet:
    print(j)
