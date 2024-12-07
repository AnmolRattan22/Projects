import random


def pass_gen(length):
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    digit = ['0','1','2','3','4','5','6','7','8','9']
    special ='!@#$%^&*()-_=+\\|[]{};:/.>?'
    genrated = random.choice(char) + random.choice(digit) + random.choice(special)
    print(genrated)
pass_gen(12)