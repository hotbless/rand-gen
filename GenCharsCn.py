import random
import string
import pyperclip

# Generate random chinese string, size para is the length of it
# TODO: Integrated with GUI


class GenCharsCn:
    # size para assigns the length of string
    def __init__(self):
        pass

    def gen_chars_cn(self, size=3):
        try:
            chars = ''
            for i in range(size):
                new_c = self.__cn_chars()
                chars = chars + new_c
        except Exception as err:
            print(err)
        else:
            # Copy to system clipboard
            pyperclip.copy(chars)
            print(chars)
            return chars

    @staticmethod
    def __cn_chars():
        try:
            head = random.randint(0xb0, 0xf7)
            body = random.randint(0xa1, 0xfe)
            val = f'{head:x}{body:x}'
            chars = bytes.fromhex(val).decode('gb2312')
        except Exception as err:
            print(err)
        else:
            return chars


if __name__ == '__main__':
    GenCharsCn().gen_chars_cn(6)

