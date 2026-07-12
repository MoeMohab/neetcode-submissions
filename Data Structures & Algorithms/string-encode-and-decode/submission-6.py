class Solution:

    def encode(self, strs: List[str]) -> str:
        if not len(strs):
            return "empty"
        vals = []
        n = len(strs)
        for s in strs:
            for c in s:
                vals.append(str(ord(c))+'?')
            n -= 1
            if n > 0:
                vals.append('|')
        return ''.join(vals)
    def decode(self, s: str) -> List[str]:
        if s=='empty':
            return []
        s_arr = s.split('|')
        res = []
        for s in s_arr:
            word = ''
            if s:
                chars = s.split('?')
                for c in chars:
                    if c:
                        word += chr(int(c))
            res.append(word)
        return res
