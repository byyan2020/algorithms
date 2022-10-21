from unittest import result


class Solution:
    def word_wrap(self, words, max_len):
        if not words:
            return []
        res = []
        i = 0
        while i < len(words):
            remain = max_len
            count = 0
            while i < len(words):
                if remain - len(words[i]) < 0:
                    break
                count += 1
                remain -= (len(words[i]) + 1)
                i += 1
            res.append(('-'.join(words[i - count: 1])))
        return res


sol = Solution()
input = ['a', 'bb', 'ccc', 'dddd']
ans = sol.word_wrap(input, 20)
print(ans)
