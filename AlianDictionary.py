from collections import deque


def createNodes(word0, word1, inorders, outorders):

    for c1,c2 in zip(list(word0), list(word1)):
        if c1 != c2:
            if c1 not in inorders:
                inorders[c1] = set()
                inorders[c1].add(c2)
            else:
                inorders[c1].add(c2)
            if c2 not in outorders:
                outorders[c2] = set()
                outorders[c2].add(c1)
            else:
                outorders[c2].add(c1)


def alianDictionary(words):

    #first find number of unique characters in vocab

    inorders = {}
    outorders = {}

    for i in range (1, len(words)):
        createNodes(words[i-1], words[i],inorders, outorders )


    charDict = set()
    for key in inorders:
        if key not in charDict:
            charDict.add(key)

    for key in outorders:
        if key not in charDict:
            charDict.add(key)

    dictSize = len(charDict)
    visited = [False for i in range(dictSize)]
    queue = deque([])
    print(inorders)
    print(outorders)

    #from this point we just have to do topological sort
    return list(words)

def main():
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    order = alianDictionary(words)
    print(order)
    words = ["apple", "appetizer", "banana", "ban", "bat"]
    order = alianDictionary(words)
    print(order)
    words = ["z", "x", "z"]
    order = alianDictionary(words)
    print(order)
    words = ["xyz", "yzx", "zyx"]
    order = alianDictionary(words)
    print(order)
main()