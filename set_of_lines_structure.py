from random import randint
import time


# функція для заповнення файла командами
def fill_file(n):
    operations = ["+", "-", "?"]
    list_of_letters = ["a", "b", "c", "d", "e", "f", "g", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                       "t", "u", "v", "w", "x", "y", "z"]
    with open("input.txt", 'w') as f:
        for i in range(0, n):
            word = ""
            for j in range(randint(1, 15)):
                word = word + list_of_letters[randint(0, len(list_of_letters) - 1)]
            word_operation = word + " " + operations[randint(0, 2)]
            f.write(word_operation + "\n")
        f.write("#")


# класс що описує структуру "множина рядків"
class SetOfLinesStructure:
    def __init__(self):
        self.body = []
        self.CONST_n = 10 ** 6

    # операція додавання
    def operation_plus(self, line):
        if len(self.body) < self.CONST_n:
            self.body.append(line)
        return

    # операція вилучення
    def operation_minus(self, line):
        if self.body.__contains__(line):
            self.body.remove(line)
            return
        else:
            return

    # перевірка наявності в структурі
    def operation_check_if_contains(self, line):
        for i in self.body:
            if i == line:
                return True
        return False

    # групування за повторюваннями
    def group_repeatable(self):
        words = []
        total_time = 0
        for i in self.body:
            start_time = time.time()
            if words.__contains__(i):
                continue
            rep = 0
            for j in self.body:
                if i == j:
                    rep += 1
            total_time += time.time() - start_time
            if rep > 1:
                print(f"Word {i} - {rep} repeats")
                words.append(i)
        print(f"Total time of grouping: {total_time} seconds")
        print(f"Time of 100 simple operations: {total_time/10000}")

    # функція для прямого заповнення структури
    def fill_n_lines(self, n):
        list_of_letters = ["a", "b", "c", "d", "e", "f", "g", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                           "t", "u", "v", "w", "x", "y", "z"]
        for i in range(0, n):
            word = ""
            for j in range(randint(10, 15)):
                word = word + list_of_letters[randint(0, len(list_of_letters) - 1)]
            self.operation_plus(word)

    # виконання операцій з файлу
    def do_commands_from_file(self):
        lines = open("input.txt").read().split('\n')
        with open("output.txt", 'w') as f:
            for i in lines:
                arr = i.split(' ')
                if arr[0] == "#":
                    break
                elif arr[1] == "+":
                    self.operation_plus(arr[0])
                elif arr[1] == "-":
                    self.operation_minus(arr[0])
                elif arr[1] == "?":
                    if self.operation_check_if_contains(arr[0]):
                        f.write(f"{arr[0]} - yes\n")
                    else:
                        f.write(f"{arr[0]} - no\n")


if __name__ == '__main__':
    struct = SetOfLinesStructure()
    fill_file(1000)
    struct.do_commands_from_file()
    struct.group_repeatable()
