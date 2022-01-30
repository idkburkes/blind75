    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b != 0:
            xor = (a^b) & mask
            carry = ((a&b) << 1) & mask
            a = xor
            b = carry
            
        if (a>>31) == 1:
            return ~(a^mask)
        else:
            return a