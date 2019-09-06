# "Triple Shuffle Cipher"
# Developed by YaF3li

class Cipher:
    def __init__(self, indexA, indexB):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self.check_index(indexA) != 1:
            raise Exception()
        if self.check_index(indexB) != 1:
            raise Exception()
        
        self.initialA = indexA
        self.initialB = indexB
        self.reset()

    def check_index(self, index):
        if len(index) != len(self.alphabet):
            return 0
        for c in index:
            if self.alphabet.find(c) < 0:
                return 0
        return 1

    def encipher(self, input):
        self.reset()
        
        output = []
        lastIndex = 0
        for c in input:
            index = ord(c) - 65
            if index >= 0 and index <= 25:
                self.shuffle(lastIndex)
                c = self.alphabet[self.get_wiring(index)]
                output.append(c)
                lastIndex = index
        return "".join(output)
    
    def decipher(self, input):
        self.reset()
        
        output = []
        lastIndex = 0
        for c in input:
            index = ord(c) - 65
            if index >= 0 and index <= 25:
                self.shuffle(lastIndex)
                index = self.get_wiring_reverse(index)
                output.append(self.alphabet[index])
                lastIndex = index
        return "".join(output)

    def get_wiring(self, index):
        c = self.indexA[index]
        return self.indexB.find(c)

    def get_wiring_reverse(self, index):
        c = self.indexB[index]
        return self.indexA.find(c)

    def shuffle(self, additive):
        if self.swapShuffle != 0:
            splice = self.indexB
            move = self.indexA
        else:
            splice = self.indexA
            move = self.indexB
        
        # Splice 1
        splice = splice[13:] + splice[:13]
        
        # Splice 2
        index = (7 + additive) % 26
        splice = splice[index] + splice[:index] + splice[index+1:]
        
        # Move
        move = move[18:] + move[:18]
        
        if self.swapShuffle != 0:
            self.indexB = splice
            self.indexA = move
        else:
            self.indexA = splice
            self.indexB = move
        
        self.swapShuffle = (self.swapShuffle + 1) % 2

    def reset(self):
        self.indexA = self.initialA
        self.indexB = self.initialB
        self.swapShuffle = 0