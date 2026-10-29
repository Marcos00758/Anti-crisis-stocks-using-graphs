class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maior_valor = 0
        i1 = 0
        i2 = 0
        s = s.lower()

        while i1 < len(s):
            verificados = set()
            i2 = i1

            while i2 < len(s):
                if s[i2] not in verificados:
                    verificados.add(s[i2])
                    i2 += 1 
                    
                else:
                    if len(verificados) > maior_valor:
                        maior_valor = len(verificados)
                    break

            i1 += 1

        return maior_valor