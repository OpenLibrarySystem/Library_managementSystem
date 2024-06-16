from random import randint


def generate_isbn():
    return str(randint(10000000, 99999999))