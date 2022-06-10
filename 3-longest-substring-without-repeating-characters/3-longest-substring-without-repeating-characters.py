class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        words = ''
        for i in s:
            if i not in words:
                words += i
            else:
                words = words[words.index(i)+1:] + i
            max_length = max(max_length, len(words))
        return max_length