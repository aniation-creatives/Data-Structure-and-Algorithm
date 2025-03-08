def all_construct(target, word_bank, memo = {}):
    if target in memo:
        return memo[target]

    if target == '':
        return [[]]

    result = []

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = [[word] + way for way in suffix_ways]
            result.extend(target_ways)

    memo[target] = result
    return result


target = "abcdef"
word_bank = ['ab', 'abc', 'cd', 'def', 'abcd', 'ef']
print(all_construct(target, word_bank))
