import math
import re

class Bayes_Classifier:

    def __init__(self):
        self.number_of_positive = 0
        self.number_of_negative = 0
        self.number_of_words_pos = 0
        self.number_of_words_neg = 0
        self.vocab = set([])
        self.number_words = {}
        

    def train(self, lines):
        count = 0
        count2 = 0
        while count < len(lines):
            line = lines[count]
            line.replace('\n', '')
            x1 = line.split('|')
            x2 = x1[0]
            text = x1[2]
            words = text.split(' ')
            while count2 < len(words):
                word = words[count2]
                key = x2 + word
                self.vocab.add(word)
                if self.number_words.get(key) !=  None:
                    self.number_words[key] = self.number_words[key] + 1
                if self.number_words.get(key) == None:
                    self.number_words[key] = 1
                count2 = count2 + 1
            if x2== "5":
                self.number_of_words_pos = self.number_of_words_pos + len(words)
                self.number_of_positive = self.number_of_positive + 1
            if x2 == "1":
                self.number_of_words_neg = self.number_of_words_neg + len(words)
                self.number_of_negative = self.number_of_negative + 1
            count = count + 1
            count2 = 0
            


    def classify(self, lines): 
        predictions = []
        count = 0
        count1 = 0
        while count < len(lines):
            line = lines[count]
            neg_total = 0
            pos_total = 0
            line.replace('\n', '')
            x1 = line.split('|')
            x2 = x1[2]
            words = x2.split(' ')
            total = float((self.number_of_negative + self.number_of_positive))
            z1 = float((self.number_of_positive) / (total))
            z2 = float((self.number_of_negative) / (total))
            while count1 < len(words):
                word = words[count1] 
                if self.number_words.get("5" + word) != None:
                    pos_total = float((self.number_words["5" + word] + 1)) / float((len(self.vocab) + self.number_of_words_pos))
                    z1 = z1 * pos_total
                if self.number_words.get("5" + word) == None:
                    pos_total = 1.0 / float((len(self.vocab) + self.number_of_words_pos ))
                    z1 = z1 * pos_total
                if self.number_words.get("1" + word) != None:
                    neg_total = float((self.number_words["1" + word] + 1)) / float((len(self.vocab) + self.number_of_words_neg))
                    z2 = z2 * neg_total
                if self.number_words.get("1" + word) == None:
                    neg_total = 1.0 / float((len(self.vocab) + self.number_of_words_neg))
                    z2 = z2 * neg_total      
                count1 = count1 + 1
            if z2 < z1:
                predictions.append("5")
            if z2 > z1:
                predictions.append("1") 
            if z2 == z1:
                predictions.append("0")
            count = count + 1
            count1 = 0
        return predictions
