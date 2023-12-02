"""Using recursion, find words that are palindromes"""

phrase = "Oo wow this kayak in deep water is on a radar peep"
palin = []

for word in phrase.split():
    if len(word) == 1:
        palin.append(word)
    else:
        full = word
        word = word.lower()
        while len(word) > 0 and word[0] == word[-1]:
            if len(word) < 3:
                palin.append(full)
            word = word[1:-1]    # removes the first and last character of the word

print(palin)
