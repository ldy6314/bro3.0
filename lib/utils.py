from datetime import datetime as dt
import os


def get_root_path():
    site_root = os.path.dirname(os.path.realpath(__file__))
    parent_root = os.path.abspath(os.path.join(site_root, os.pardir))
    return parent_root


def current_time_str():
    tm = dt.now()
    return tm.strftime("%H:%M:%S"), tm.weekday()


def parse_to_time(number):
    h = number // 3600
    number %= 3600
    m = number // 60
    number %= 60
    s = number
    return h, m, s


def to_time_str(number):
    if number == -1:
        return "暂无任务"
    return "{:02}:{:02}:{:02}".format(*parse_to_time(number))


def time_to_number(the_time):
    h, m, s = map(int, the_time.split(':'))
    return h * 3600 + m * 60 + s


def parse_to_weekdays(number):
    res = []
    for i in range(7):
        if number & (1 << i):
            res.append(i + 1)
    return tuple(res)


def weekdays_to_number(weekdays):
    if len(weekdays) == 1:
        lst = (int(weekdays))
    else:
        lst = eval("(" + weekdays + ")")
    res = 0
    for i in lst:
        res += 1 << i - 1
    return res


if __name__ == '__main__':
    print(parse_to_weekdays(42))
    print(current_time_str())
