class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list_of_words):
        matches = []
        for current_word in list_of_words:
            letter_list = [letter for letter in current_word]
            if sorted(letter_list) == sorted(self.word):
                matches.append(current_word)
            
        return matches
