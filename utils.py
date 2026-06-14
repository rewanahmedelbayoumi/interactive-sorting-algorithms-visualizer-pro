import random

def generate_array(size):
    return [random.randint(10, 100) for _ in range(size)]