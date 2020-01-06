def sherlockAndAnagrams(s):
    cnt = 0
    for l in range(1, len(s)):
        words = {}
        for i in range(len(s)-l+1):
            sub = list(s[i:i+l])
            sub.sort()
            sub = ''.join(sub)
            if sub in words:
                cnt += words[sub]
                words[sub] += 1
            else:
                words[sub] = 1
    return cnt
