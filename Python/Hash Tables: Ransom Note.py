def checkMagazine(magazine, note):
    words = {}
    for i in magazine:
        words[i] = words.get(i, 0) + 1
    for i in note:
        if i not in words:
            print('No')
            return
        else:
            words[i] -= 1
            if words[i] < 0:
                print('No')
                return
    print('Yes')
