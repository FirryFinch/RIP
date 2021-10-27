import time
from contextlib import contextmanager


class cm_timer_1:

    def __init__(self):
        self.timer = time.time()

    def __enter__(self):
        pass

    def __exit__(self, exp_type, exp_value, traceback):
        self.timer = time.time() - self.timer
        print('time: {}'.format(self.timer))


@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    end_time = time.time() - start_time
    print('time: {}'.format(end_time))


if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
        time.sleep(5.5)
