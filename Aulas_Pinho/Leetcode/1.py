class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indice1 = 0

        for numero in nums:
            indice2 = 0

            for alvo in nums:

                if numero + alvo == target and indice1 != indice2:
                    return [indice1, indice2]
                indice2 += 1
            indice1 += 1
