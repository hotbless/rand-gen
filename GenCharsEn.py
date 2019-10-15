import random
import string
import pyperclip

# Generate random english string
# TODO: Integrated with GUI


class GenCharsEn:
    # size para assigns the length of string
    def __init__(self, size=10):
        try:
            # Better than string.printable, avoid ascii can't display correctly
            self.chars = string.digits + string.ascii_lowercase + \
                    string.ascii_uppercase + string.punctuation
            cha_gen = ''.join(random.choices(self.chars, k=size))
        except Exception as err:
            print(err)
        else:
            # Copy to system clipboard
            pyperclip.copy(cha_gen)
            print(cha_gen)
            return cha_gen


if __name__ == '__main__':
    GenCharsEn(20)





