import json
import sys
import cm_timer
from print_result import print_result
from gen_random import gen_random

with open('C:\\Users\\antsi\\OneDrive\\Документы\\МГТУ\\5 семестр\\РИП\\Лаб3\\lab_python_fp\\data_light.json', encoding='utf8') as a:
    data = json.load(a)

@print_result
def f1(d):
     return sorted(set([val.lower() for val in d]), key=str.lower)


@print_result
def f2(d):
    return list(filter(lambda a: str.startswith(a, 'программист'), d))


@print_result
def f3(d):
    return list(map(lambda a: a + ' с опытом Python', d))


@print_result
def f4(d):
    temp = list(zip(d, [(', зарплата '+ str(el) + ' руб.') for el in list(gen_random(len(d), 100000, 200000))]))
    return [(el[0]+el[1]) for el in temp]


if __name__ == '__main__':
     with cm_timer.cm_timer_1():
         f4(f3(f2(f1([el['job-name'] for el in data]))))