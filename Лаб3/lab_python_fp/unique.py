from gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.elems = set()
        self.data = items
        self.index = 0

        if 'ignore_case' not in kwargs.keys():
            self.ignore_case = False
        else:
            self.ignore_case = kwargs['ignore_case']

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index < len(self.data):
                current = self.data[self.index]
                self.index = self.index + 1
                if self.ignore_case:
                    if current.lower() not in self.elems:
                        self.elems.add(current.lower())
                        return current
                else:
                    if current not in self.elems:
                        self.elems.add(current)
                        return current
            else:
                raise StopIteration
                
if __name__ == "__main__":
    print ('Тест 1 - [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]')
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for el in Unique(data):
        print(el)
    print ('Тест 2 - gen_random(1, 3, 10)')
    data = gen_random(1, 3, 10)
    for el in Unique(data):
        print(el)
    print ('Тест 3 - [\'a\', \'A\', \'b\', \'B\', \'a\', \'A\', \'b\', \'B\'] и Unique(data)')
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for el in Unique(data):
        print(el)
    print ('Тест 4 - [\'a\', \'A\', \'b\', \'B\', \'a\', \'A\', \'b\', \'B\'] и Unique(data, ignore_case=True)')
    for el in Unique(data, ignore_case=True):
        print(el)