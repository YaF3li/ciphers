# "Kotzelfoa"
# by Garrett Warren
# Program by YaF3li

class Code:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.vowels = "AEIOU"
        self.vowel_separator = 't'
        self.single_letter_indicator = 'p'
        self.codeA = ["z", "sm", "sp", "g", "f", "v", "sh", "m", "sk", "b", "ch", "shk", "d", "jh", "j", "s", "sf", "tz", "st", "n", "h", "shl", "k", "th", "fl", "shp"]
        self.codeB = ["o", "ail", "oi", "al", "i", "ai", "ar", "ia", "u", "or", "oil", "ol", "oe", "oa", "a", "er", "oal", "el", "il", "ir", "e", "ial", "oar", "oel", "iar", "ul"]
        self.codes = [self.codeA, self.codeB]

    def next_token(self, input, position, code):
        token = input[position : position + 3]
        while not (token in code):
            token = token[0 : len(token) - 1]
            if len(token) <= 0:
                return "", position + 1
        return token, position + len(token)
    
    def encode(self, input):
        input = input.upper()
        
        output = ""
        for word in input.split():
            if len(word) <= 0:
                continue
            if len(word) <= 1:
                charIdx = self.alphabet.find(word[0])
                if charIdx >= 0:
                    output += self.single_letter_indicator + self.codeB[charIdx] + " "
                continue
            bigrams = [[]]
            for c in word:
                charIdx = self.alphabet.find(c)
                if charIdx >= 0:
                    idx = len(bigrams) - 1
                    if len(bigrams[idx]) >= 2:
                        bigrams.append([])
                        idx += 1
                    bigrams[idx].append(charIdx)
            
            for bigram in bigrams:
                if len(bigram) < 2:
                    lastChar = output[len(output) - 1].upper()
                    if self.vowels.find(lastChar) >= 0:
                        output += self.vowel_separator
                    output += self.codeB[bigram[0]]
                else:
                    output += self.codeA[bigram[0]]
                    output += self.codeB[bigram[1]]
            output += " "
        return output
    
    def decode(self, input):
        input = input.lower()
        
        output = ""
        for word in input.split():
            if len(word) <= 0:
                continue
            if len(word) <= 2 and word[0] == self.single_letter_indicator:
                if word[1] in self.codeB:
                    idx = self.codeB.index(word[1])
                    output += self.alphabet[idx]
                output += " "
                continue
            
            position = 0
            code = 0
            while position < len(word):
                lastPosition = position
                token, position = self.next_token(word, position, self.codes[code])
                if position >= len(word):
                    code = 1
                    token, position = self.next_token(word, lastPosition, self.codes[code])
                if len(token) > 0:
                    idx = self.codes[code].index(token)
                    output += self.alphabet[idx]
                code = (code + 1) % 2
            output += " "
        return output