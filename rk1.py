# Для сортировки
from operator import itemgetter
 
class Comp:
    """Компьютер"""
    def __init__(self, id, name, ser, class_id):
        self.id = id
        self.name = name
        self.ser = ser
        self.class_id = class_id
 
class DispCl:
    """Дисплейный класс"""
    def __init__(self, id, numb):
        self.id = id
        self.numb = numb
 
class CompDisp:
    """
    'Компьютеры в дисплейных классах' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, class_id, comp_id):
        self.class_id = class_id
        self.comp_id = comp_id
 
# Дисплейные классы
classes = [
    DispCl(1, '404'),
    DispCl(2, '113'),
    DispCl(3, '41'),
    DispCl(4, '362'),
    DispCl(5, '511'),
]
 
# Компьютеры
comps = [
    Comp(1, 'HP', '1AAA01', 1),
    Comp(2, 'DELL', '2BBB02', 1),
    Comp(3, 'DELL', '3CCC03', 4),
    Comp(4, 'TOSHIBA', '4DDD04', 2),
    Comp(5, 'ASUS', '5EEE05', 5),
]
 
 # Компьютеры и дисплейные классы (для "многих ко многим")
compsindisps = [
    CompDisp(1,1),
    CompDisp(1,2),
    CompDisp(2,4),
    CompDisp(4,3),
    CompDisp(5,5),
]
 
def main():
    """Основная функция"""
 
    # Соединение данных один-ко-многим 
    one_to_many = [(comp.name, comp.ser, cl.numb) 
        for comp in comps 
        for cl in classes 
        if comp.class_id==cl.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(cl.numb, ccl.class_id, ccl.comp_id) 
        for cl in classes 
        for ccl in compsindisps 
        if cl.id==ccl.class_id]
    
    many_to_many = [(comp.ser, numb) 
        for numb, comp_id, class_id in many_to_many_temp
        for comp in comps 
        if (comp.id==comp_id)]
 
    print('Задание 1')
    res_1 = sorted(one_to_many, key=itemgetter(2))
    print(res_1)
    
    print('\nЗадание 2')
    res_2_unsorted = []
    # Перебираем все дисплейные классы
    for c in classes:
        # Количество компьютеров в классах
        kol = sum ([comp.id for comp in comps if (comp.class_id == c.id)])
        res_2_unsorted.append((c.numb, kol))
 
    # Сортировка по возрастанию
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    print(res_2)
 
    print('\nЗадание 3')
    res_3 = {}
    # Перебираем все дисплейные классы
    for c in classes:
        if '1' in c.numb:
            # Список классов с цифрой "1"
            listcl = list(filter(lambda a: a[1] == c.numb, many_to_many))
            # Только серийные номера компьютеров
            lisclcomp = [x for x,_ in listcl]
            res_3[c.numb] = lisclcomp
    print(res_3)
 
if __name__ == '__main__':
    main()