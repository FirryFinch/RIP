# Пример:
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
# Hint: типовая реализация занимает 2 строки

from random import randrange

def gen_random(count, min, max):
    return [randrange(min, max+1) for i in range(count)]
    
if __name__ == "__main__":
    print (gen_random(5, 1, 3))