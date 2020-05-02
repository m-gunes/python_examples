class File:
    def __init__(self):
        with open('text.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split() # birsey vermezsek bosluga gore split eder
            self.just_words = list()

            for i in words:
                i = i.strip('\n')
                i = i.strip(' ')
                i = i.strip('.')
                i = i.strip(',')
                self.just_words.append(i)

    def all_words(self):
        sets_words = set()
        for i in self.just_words:
            sets_words.add(i)

        for i in sets_words:
            print(i)
    def words_count(self):
        words_dict = dict()
        for i in self.just_words:
            if i in words_dict:
                words_dict[i] += 1
            else:
                words_dict[i] = 1

        for word, count in words_dict.items():
            print('{} kelimesi {} defa geciyor'.format(word, count))
            print('--------------------------------')







file1 = File()
# file1.all_words()
file1.words_count()