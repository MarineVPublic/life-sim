from life_sim.colleagues import *

def main():
    alice = Colleague("Alice", 80, 30)

    alice.display()
    alice.decrease_needs()
    alice.display()


if __name__ == '__main__':
    main()