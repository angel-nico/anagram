def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = 'listen'
    anagram = 'silent'
    # check if length is same
    if (len(word)) == len(anagram):
        sorted_word = sorted(word)
        sorted_anagram = sorted(anagram)

        if (sorted_word == sorted_anagram):
            return True

        else:
            return False


