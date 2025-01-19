def isAnagram(s1, s2):

    charMap = {}
    #first if string of different length they are not anagram
    if len(s1)!= len(s2):
        return False
    s1 = list(s1)
    s2 = list(s2)
    for char in s1:
        if char not in charMap:
            charMap[char] = 1
        else:
            charMap[char]  = charMap[char] + 1

    #now we will remove these counts. by end we should have charMap of zero size
    for char in s2:
        if char in charMap:
            charMap[char] = charMap[char] - 1
            if charMap[char] == 0:
                del charMap[char]
        else:
            return False

    if len(charMap) == 0:
        return True
    else:
        return False

def main():
    s= "racecar"
    t = "carrace"
    print(isAnagram(s, t))

    s = "jar",
    t = "jam"
    print(isAnagram(s, t))


main()