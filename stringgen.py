import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def main():
    length = int(input('Enter string length: '))
    print(generate_string(length))


def generate_string(length):
    text = ''
    for i in range(length):
        index = random.randint(0, len(LETTERS) - 1)
        text += LETTERS[index]
    return text


if __name__ == '__main__':
    main()
