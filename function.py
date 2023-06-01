def is_ordered_word(word, LETTERS):
    const = 0
    count = 0
    for i in range(len(word)):
        if word[i].lower() not in LETTERS:
            raise ValueError('The word contains invalid characters')
        if i == 0:
            const = LETTERS[word[i].lower()]
            count = 1
        else:
            if const < LETTERS[word[i].lower()]:
                const = LETTERS[word[i].lower()]
                count += 1
            else:
                return False
    if count == len(word):
        return True
    else:
        return False 