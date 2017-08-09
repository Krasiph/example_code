import random
import argparse


D6 = [1, 2, 3, 4, 5, 6]


def roll_attack():
    d1 = random.choice(D6)
    d2 = random.choice(D6)
    sd = random.choice(D6)
    
    sum = d1 + d2 + sd
    
    if d1 == d2 or d1 == sd or d2 == sd:
        return sum, sd
    else:
        return sum, 0


if __name__ == '__main__':
    random.seed()
    
    parser = argparse.ArgumentParser(description='Roll attacks for the Hydra.')
    parser.add_argument('heads', type=int, help='the number of heads the Hydra currently has')

    args = parser.parse_args()
    
    for i in range(0, args.heads):
        print(roll_attack())
