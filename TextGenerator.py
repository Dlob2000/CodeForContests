import random
import re
import pickle

class TextGenerator:
    
    def __init__(self):
        self.d = dict()
    
    def save(self):
        with open('data.pickle', 'wb') as f:
            pickle.dump(self, f)

    def load(self):
        with open('data.pickle', 'rb') as f:
            a = pickle.load(f)
        self.d = a.get_d()

    def _parse_text(self, text):
        reg = re.compile("\w+")
        return reg.findall(text)

    def fit(self, path):
        with open(path, 'r', encoding="utf-8") as f:
            text = self._parse_text(f.read())
        
        prev = None
        for word in text:
            if prev:
                if prev in self.d.keys():
                    self.d[prev] += [word]
                else:
                    self.d[prev] = [word]
            prev = word
            
    def get_d(self):
        return self.d
    
    def generate(self, long):
        first = random.choice(list(self.d.keys()))
        current = first
        string = ""
        is_title = True
        for i in range(long):
            if current in self.d.keys():
                a = random.choice(self.d[current])               
                if is_title:
                    string += "{} ".format(current.title())
                else:
                    string += "{} ".format(current)
                current = a
                is_title = False
            else:
                string = string[0:-1] + ". "
                current = random.choice(list(self.d.keys()))
                is_title = True
        return string[0:-1] + "."