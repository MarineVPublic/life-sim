import random
from colleagues import Colleague

#random.shuffle shuffle names in the list to distribute them as randomly
#the for name in name_list return one name from the list
def names_generator():
    name_list = ['Alice', 'Bob', 'Charlie']
    random.shuffle(name_list)
    for name in name_list:
        yield name

name_generator_instance = names_generator()

#Only 3 colleagues max can be generated as we choose a name in the list limited to 3 names
def colleagues_generator():
    for name in name_generator_instance:
        colleague = Colleague(name, 100, 100)
        yield colleague

colleague_generator_instance = colleagues_generator()

#we can ask for 3 colleagues max as we have only 3 names.
#if we request 5 colleagues for exemple, we'll have an error
colleagues = [next(colleague_generator_instance) for _ in range(3)]
print(colleagues)