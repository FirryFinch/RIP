def print_result(func):
    def myfunc(*args):
        pars = func(*args)
        
        print(func.__name__)
        if isinstance(pars, dict):
            for key, p in pars.items():
                print('{} = {}'.format(key, p))
        elif isinstance(pars, list):
            for p in pars:
                print(p)
        else:
            print(pars)
        return pars
    return myfunc


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()