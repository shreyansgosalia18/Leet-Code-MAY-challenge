"""Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true"""


class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = dict([])
        lr = list(ransomNote)
        lm = list(magazine)
        for i in range(len(lm)):
            if lm[i] in cnt.keys():
                cnt[lm[i]] += 1
            else:
                cnt[lm[i]] = 1
        for i in range(len(lr)):
            if lr[i] not in cnt.keys() or cnt[lr[i]] == 0:
                return False
            cnt[lr[i]] -= 1
        return True