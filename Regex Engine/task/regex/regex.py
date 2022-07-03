class Regex:

    def main(self, regex, word):
        if regex == '.*' and len(word) > 0 or regex == '.?' and len(word) >= 0:
            return True
        elif regex == '.+' and len(word) >= 1:
            return True
        elif '^' in regex and '+' in regex and '$' in regex:
            regexes = regex.split('+')
            if self.start(regexes[0], word) and self.end(regexes[1], word):
                return True
            return False
        elif '^' in regex and '$' in regex:
            if self.start(regex, word):
                if self.end(regex, word):
                    return True
            return False
        elif '^' in regex:
            if self.start(regex, word):
                return True
            return False
        elif '$' in regex:
            if self.end(regex, word):
                return True
            return False
        if self.check_word(regex, word):
            return True
        return False

    def start(self, regex, word):
        regex = regex.strip('^$')
        word = word[:len(regex)]
        if self.check_word(regex, word):
            return True
        return False

    def end(self, regex, word):
        regex = regex.strip('^$')
        if '\\' in regex:
            word = word[-len(regex) + 1:]
        else:
            word = word[-len(regex):]
        if self.check_word(regex, word):
            return True
        return False


    def check_word(self, regex, word):
        regex = ' ' if regex == '' else regex
        word = ' ' if word == '' else word
        for letters in word:
            if self.character_check(regex, word):
                return True
            word = word[1:]
        return False


    def zero_one(self, regex, word):
        return regex.split('?')[1] , word


    def zero_many(self, regex, word):
        regex = regex.split('*')[1]
        return regex, word[word.index(regex[0]):]

    def one_many(self, regex, word):
        regex = regex.split('+')[1]
        if regex == '':
            regex, word = 'e', 'e'
        else:
            word = word[word.index(regex[0]):]
        return regex, word



    def character_check(self, regex, word):
        if regex[0] == '\\':
            escape = True
            regex = regex[1:]
        else:
            escape = False
        if regex[0] == '.' or regex[0] == ' ' or regex[0] == ' ' and word[0] == ' ' or regex[0] == word[0]:
            if len(regex) > 1:
                if '*' in regex[:2] and not escape:
                    return self.character_check(*self.zero_many(regex, word))
                elif '+' in regex[:2] and not escape:
                    return self.character_check(*self.one_many(regex, word))
                else:
                    return self.character_check(regex[1:], word[1:])
            else:
                return True
        elif len(regex) > 1:
            if '?' in regex[:2] and not escape:
                if regex[0] == '.' or regex[0] == '+':
                    return True
                return self.character_check(*self.zero_one(regex, word))
            elif '*' in regex[:2] and not escape:
                return self.character_check(*self.zero_many(regex, word))
            else:
                return False
        return False


regex_check = Regex()
regex_user, word_user = input().split('|')
result = regex_check.main(regex_user, word_user)
print(result)
