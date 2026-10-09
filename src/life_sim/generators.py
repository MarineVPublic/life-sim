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

def create_colleague(name:str):
    """
    Create a colleague with a name choosed in a list, a random energy level and a random social level.
    Name is generated from names_generator.
    :return:
    """
    return Colleague(
            name,
            #next(name_generator_instance),
            random.randint(0, 100),
            random.randint(0, 100)
    )