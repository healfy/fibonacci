class Fibonacci:
    def __init__(self, end):
        self.counter = end
        self.curFib = 0
        self.next_fib = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == 0:
            raise StopIteration

        self.counter -= 1

        next_fib = self.curFib + self.next_fib
        self.curFib = self.next_fib
        self.next_fib = next_fib

        return self.curFib


class ReversedFibonacci:

    def __init__(self, end):
        self.collection = self.__init_collection(end)
        self.counter = end

    @staticmethod
    def __init_collection(end: int):
        collection = [0] * end
        collection[0] = 0
        collection[1] = 1
        for i in range(2, end):
            collection[i] = collection[i - 2] + collection[i - 1]
        return collection

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == 0:
            raise StopIteration
        self.counter -= 1
        return self.collection[self.counter]
