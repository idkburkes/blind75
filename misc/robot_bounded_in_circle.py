class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = (0,1)
        dirs = [(0,1),(-1,0),(0,-1),(1,0)]
        pos = (0,0)
        
        for instr in instructions:
            if instr == 'G':
                x,y = pos
                pos = (x+direction[0],y+direction[1])
            elif instr == 'L':
                direction = dirs[(dirs.index(direction) + 1) % 4]
            else:
                direction = dirs[dirs.index(direction) - 1]
                
        return direction != (0,1) or pos == (0,0) 
        