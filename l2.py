from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy as np


def main():
    r = Rectangle("синий", 4, 4)
    c = Circle("зелёный", 4)
    s = Square("красный", 4)
    print(r)
    print(c)
    print(s)
    
    a = np.array([1, 2, 3])
    print('\nТест NumPy. Массив a -', a)

    input("\nДля завершения нажмите Enter")


if __name__ == "__main__":
    main()