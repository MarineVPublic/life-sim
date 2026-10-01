from src.life_sim.colleagues import Colleague

def hello() -> str:
    return "Hello from life-sim!"


def main():
    alice = Colleague("Alice", 80, 30)
    print(alice.name)
    print(alice.energy)
    print(alice.social_need)

if __name__ == '__main__':
    main()