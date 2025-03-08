def can_construct(word_bank, target, memo = {}):
    if target in memo:
        return memo[target]

    if target == '':
        return True

    for word in word_bank:
        if target.startswith(word):
            suffix = target.removeprefix(word)
            if can_construct(word_bank, suffix):
                memo[target] = True
                return True
    memo[target] = False
    return False


target = "abcdef"
word_bank = ['ab', 'abc', 'cd' , 'def', 'abcd']
print(can_construct(word_bank, target))