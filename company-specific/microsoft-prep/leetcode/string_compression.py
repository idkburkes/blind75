class Solution:
    def compress(self, chars: List[str]) -> int:
        # use an extra blank space to handle last char
        chars.append(' ')
        
        start = write = 0
        
        for i in range(len(chars)):
            # only take action when there is a difference
            if chars[i] != chars[start]:
                chars[write] = chars[start]
                write += 1
                # find count by checking difference in indices since the last interruption
                count = i - start
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                start = i
        
        return write
        
        