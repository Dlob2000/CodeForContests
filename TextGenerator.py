import random

class TextGenerator:
    
    def __init__(self):
        self.d = dict()
    
    def fit(self, text):
        text = text.replace(",", "").replace("\n", " ").replace(".", "").replace("?", "").lower()
        text = text.split(" ")
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
        first = random.choice(list(self.d.keys())).title()
        current = first
        string = ""
        for i in range(long):
            if current.lower() in self.d.keys():
                a = random.choice(self.d[current.lower()])
                string += "{} ".format(a)
                current = a
            else:
                string += ". "
                current = random.choice(list(self.d.keys())).title()
        return string