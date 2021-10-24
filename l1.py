import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
    if ((index == 1) & (float(coef_str) == 0)):
           while (float(coef_str) == 0):
                print('Коэффициент A не может быть равен 0!')
                print(prompt)
                coef_str = input()
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b*b - 4*a*c
    print('\nДискриминант равен =', D)
    if D == 0.0:
        if (-b / (2.0*a) > 0):
            root1 = math.sqrt(-b / (2.0*a))
            root2 = -math.sqrt(-b / (2.0*a))
            result.append(root1)
            result.append(root2)
    elif D > 0.0:
        sqD = math.sqrt(D)
        if ((-b + sqD) / (2.0*a) > 0):
            root1 = math.sqrt((-b + sqD) / (2.0*a))
            root2 = -math.sqrt((-b + sqD) / (2.0*a))
            result.append(root1)
            result.append(root2)
        if ((-b - sqD) / (2.0*a) > 0):
            root3 = math.sqrt((-b - sqD) / (2.0*a))
            root4 = -math.sqrt((-b - sqD) / (2.0*a))
            result.append(root3)
            result.append(root4)     
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1,'Введите коэффициент А:')
    b = get_coef(2,'Введите коэффициент B:')
    c = get_coef(3,'Введите коэффициент C:')
    print('\nКоэффициент A =', a)
    print('Коэффициент B =', b)
    print('Коэффициент C =', c)
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('\nНет корней')
    elif len_roots == 2:
        print('\nДва корня: ±{}'.format(roots[0]))
    elif len_roots == 4:
        print('\nЧетыре корня: ±{} и ±{}'.format(roots[0], roots[2]))
    input("\nДля завершения нажмите Enter")
    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()