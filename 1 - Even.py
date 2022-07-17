import time
t_start = time.process_time()

''' 
    я не знаю как обьяснить, что из них быстрее или лучше, знаю, что можно сравнить побайтово,
    если число кончается на 0, то оно четное, если на 1 - нечетное. Оба алгоритма О(1)
'''

def is_even1(value):
    if value & 1 and type(value) == int:
        return "нечетное"
    else:
        return 'четное'


def is_even2(value):
    return value % 2 == 0


print(is_even1(6))
print(is_even2(6))

