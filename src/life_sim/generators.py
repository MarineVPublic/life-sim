import random
from colleagues import Colleague

def names_generator():
    """
    Randomly pickup a name in the list.
    A name can be picked multiple times.
    :return:
    """
    name_list = ['Alice', 'Bob', 'Charlie']
    while True:
        yield random.choice(name_list)

name_generator_instance = names_generator()

def colleagues_generator():
    """
    Create a colleague with a name, an energy level and a social level.
    Name is generated from names_generator.
    :return:
    """
    while True:
        colleague = Colleague(next(name_generator_instance), 100, 100)
        yield colleague

colleague_generator_instance = colleagues_generator()

colleagues = [next(colleague_generator_instance) for _ in range(3)]
print(colleagues)