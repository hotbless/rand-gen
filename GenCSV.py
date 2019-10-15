import csv
from GenCharsCn import GenCharsCn as gccn
import random

class GenCSV:

    def __init__(self):
        csv_name = self.__gen_csv_name()
        self.__write_csv(csv_name, char_len=5, row=9)

    def __gen_csv_name(self):
        str_suffix = str(random.randint(100, 999))
        file_name = 'temp' + str_suffix + '.csv'
        return file_name

    def __write_csv(self, csvn, char_len, row=3):
        try:
            with open(csvn, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                for i in range(row):
                    list_cont = []
                    cont = gccn().gen_chars_cn(char_len)
                    list_cont.append(cont)
                    csv_writer.writerow(list_cont)
        except Exception as err:
            print(err)
        else:
            pass




if __name__ == "__main__":
    GenCSV()