import random
import time
import string

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'


def main():
    length = int(input('Enter string length: '))
    start_time = time.time()
    print(generate_string(length))
    total_time = time.time() - start_time
    print(f'time: {round(total_time, 3)} seconds')


def generate_string(length):
    text = ''

    for i in range(length):
        index = random.randint(0, len(SYMBOLS) - 1)
        text += SYMBOLS[index]

    return text


if __name__ == '__main__':
    main()
