import string
from sys import stdin, stderr, stdout, exit


def decoder(text: str) -> str:
    initial = 'abcdefghijklmnopqrstuvwxyz'
    initial += initial.upper()
    rotated = 'nopqrstuvwxyzabcdefghijklm'
    rotated += rotated.upper()

    decoded = ''
    for i in text:
        if i in initial:
            decoded += initial[rotated.index(i)]
        elif i in string.digits or i in string.whitespace or i in string.punctuation:
            decoded += i
        else:
            stderr.write('String must contain only Latin alphabet, digits and special characters\n')
            raise ValueError('String must contain only Latin alphabet, digits and special characters')
    return decoded


if __name__ == '__main__':
    try:
        stdout.write(f'Decoded text is: {decoder(stdin.readline())}\n')
    except:
        exit(1)
    else:
        exit(0)
