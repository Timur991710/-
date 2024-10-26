import string

from gevent.subprocess import value


class WordsFinder:
    def __init__(self, *file_names: tuple):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding="utf-8") as file:
                send = []
                for line in file:
                    line = line.translate(str.maketrans("", "", string.punctuation))
                    line = line.split()
                    for j in line:
                        send.append(j.lower())
            all_words[i] = send
        return all_words

    def finds(self, world):
        all_words_2 = {}
        for key in self.get_all_words():
            x = self.get_all_words()[key]
            for i in x:
                if i== world:

                    all_words_2[key] = x.index(i) + 1
        print(all_words_2)

        #print(self.get_all_words())


            # return all_words_2




    def counts(self, world):
        all_words_3 = {}
        for key, value in self.get_all_words().items():
            x = 0
            for i in value:
                if i== world:
                    x += 1
                all_words_3[key] = x
        return all_words_3

if __name__ == "__main__":
    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.finds('the'))
    print(finder1.counts('the'))