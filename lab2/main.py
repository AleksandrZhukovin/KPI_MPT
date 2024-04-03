import string


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
            raise ValueError('String must contain only Latin alphabet, digits and special characters')
    return decoded


if __name__ == '__main__':
    print(f'Decoded text is: {decoder(input("Enter encoded text: "))}')
