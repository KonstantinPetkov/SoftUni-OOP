class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.iterator = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterator == self.number - 1:
            raise StopIteration
        self.iterator += 1

        return self.sequence[self.iterator % len(self.sequence)]