class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        i = 1
        total1 = 0
        total2 = 0

        while l1:
            total1 += l1.val*i
            i *= 10
            l1 = l1.next
        
        i = 1

        while l2:
            total2 += l2.val*i
            i *= 10
            l2 = l2.next
        
        total = str(total1 + total2)
        total = total[::-1]
            
        lista = ListNode()
        atual = lista
        for numero in total:
            atual.next = ListNode(int(numero))
            atual = atual.next
        
        return lista.next