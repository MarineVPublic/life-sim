from life_sim.colleagues import *
from life_sim.generators import create_colleague


def main():
    alice = create_colleague("Alice")
    bob = create_colleague("Bob")
    remi = create_colleague("Rémi")

    alice.display()
    bob.display()
    remi.display()
    alice.decrease_needs()
    alice.display()

    bob.toRest()
    bob.display()
    alice.toDiscuss(remi)
    alice.display()
    remi.display()


if __name__ == '__main__':
    main()