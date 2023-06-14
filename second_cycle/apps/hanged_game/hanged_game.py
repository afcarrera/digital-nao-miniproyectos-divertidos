class HangedGame(object):
    def __init__(self) -> None:
        self.words = list()
        self.add_word('PERRO','ANIMAL DOMÉSTICO')
        self.add_word('BOSNIA Y HERZEGOVINA','PAÍS DE EUROPA')
        self.add_word('PYTHON', 'LENGUAJE DE PROGRAMACIÓN')
        
    def add_word(self, word, hint):
        temp = dict()
        for i, l in enumerate(word):
            if temp.get(l) is None:
                temp[l] = []
            temp[l].append(i)
        self.words.append([word, hint, temp])
        
    def get_words(self):
        return self.words