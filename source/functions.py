from pprint import pprint
import numpy as np

# initializing blocks (on sep. lines for clarity)
block1 = set()
block2 = set()
block3 = set()
block4 = set()
block5 = set()
block6 = set()
block7 = set()
block8 = set()
block9 = set()
block10 = set()
block11 = set()
block12 = set()
block13 = set()
block14 = set()
block15 = set()
blocks = [block1, block2, block3, block4, block5,
          block6, block7, block8, block9, block10,
          block11, block12, block13, block14, block15]


def isValid(block, letter):
    """
    returns true if letter can be added to block
    false otherwise
    """
    if letter in block:
        return False
    if len(block) >= 6:
        return False
    return True


def canWriteRec(word, blocklist):
    """
    return 1 if word can be spelled with blocklist
    0 otherwise
    """
    if len(word) > 1:
        letter = word[0]
    else:
        letter = word
    if letter == ' ':
        word = word[1:]
        if len(word) > 1:
            letter = word[0]
        else:
            letter = word
    options = []
    for block in blocklist:
        if letter in block:
            options.append(block)
    if len(options) == 0:
        return 0
    if len(word) == 1:  # on last letter and there are options left
        return 1
    for block in options:
        x = canWriteRec(word[1:], [i for i in blocklist if i != block])
        if x == 1:
            return 1
    return 0


def createBlocksRec(word, blocklist):
    """
    Modifies the blocks in the blocklist so that
    they can spell the given word, by adding letters
    (or doing nothing if the word can already be spelled)
    Function is recursive and not completely efficient
    with its use of letters, hence the optimization
    function later
    """
    if len(word) > len(blocklist):
        return 0
    if canWriteRec(word, blocklist):
        return 1
    if len(word) > 1:
        letter = word[0]
    else:
        letter = word
    if letter == ' ':
        x = createBlocksRec(word[1:], blocklist)
        if x == 1:
            return 1
        else:
            return 0
    valid = []
    for block in blocklist:
        if isValid(block, letter):
            valid.append(block)
    if not valid:
        return 0
    if len(word) > 1:
        for block in valid:
            if canWriteRec(word[1:], [b for b in blocklist if b != block]):
                index = blocklist.index(block)
                blocklist[index].add(letter)
                return 1
            if canWriteRec(word[1:-1], [b for b in blocklist if b != block]):
                letter = word[-1]
                index = blocklist.index(block)
                blocklist[index].add(letter)
                if canWriteRec(word[1:], [b for b in blocklist if b != block]):
                    return 1
                else:
                    continue
    value = min(valid, key=len)
    index = blocklist.index(value)
    blocklist[index].add(letter)
    if len(word) == 1:
        return 1
    else:
        x = createBlocksRec(word[1:], [b for b in blocklist if b != blocklist[index]])
        if x == 1:
            return 1
        else:
            return 0


def lettersUsed():
    """
    prints the total number of letters used on the blocks
    """
    print("Letters used:", sum([len(s) for s in blocks]))


def userCanWrite():
    """
    allows user to check if certain words
    and phrases can be made with the blocks
    """
    while True:
        word = input("Enter word (or end to stop): ")
        if word == "break" or word == "end":
            return
        x = canWriteRec(word, blocks)
        if x == 1:
            print("yep")
        else:
            print("nope")


def makeblocklist():
    """
    converts the blocks to lists and makes a
    list of blocks. Does not modify original
    blocks, which are sets
    """
    global blocklist
    blocklist = []
    for block in blocks:
        blocklist.append(list(block))


def optimize(wordlist):
    """
    given a list of words, this function prunes
    the blocks, removing any letters not needed
    to spell the given words.
    """
    print("Optimizing...")
    col = 0
    removed = 0

    while col < 6:
        row = -1

        while row < 14:
            row += 1
            makeblocklist()
            lblock = blocklist[row]
            if len(lblock) <= col:
                continue
            letter = lblock[col]

            temp = []
            for a in blocklist:
                temp2 = []
                if a != lblock:
                    temp.append(a)
                else:
                    temp2 = []
                    for l in lblock:
                        if l != letter:
                            temp2.append(l)
                temp.append(temp2)
            result = 0
            for word in wordlist:
                if canWriteRec(word, temp) == 1:
                    result += 1
            if result == len(wordlist):
                removed += 1
                blocks[row].remove(letter)

        col += 1
    print("Letters removed in optimization:", removed)


def canSpell(wordlist):
    """
    returns the number of words in the wordlist
    that can be written with the blocks
    """
    result = 0
    for word in wordlist:
        if canWriteRec(word, blocks) == 1:
            result += 1
    return result


def addWords(wordlist, words):
    """
    adds words in first arg to second arg,
    then updates the blocks for the new wordlist
    """
    for word in wordlist:
        words.append(word)
    while canSpell(words) < len(words):
        for word in words:
            createBlocksRec(word, blocks)

