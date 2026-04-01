class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        
        # sort by position
        robots = sorted([(positions[i], healths[i], directions[i], i) for i in range(n)])
        
        stack = []  # indices in robots list
        
        # convert to list so we can update health
        healths = [r[1] for r in robots]
        
        for i in range(n):
            pos, h, d, idx = robots[i]
            
            if d == 'R':
                stack.append(i)
            else:  # d == 'L'
                while stack and healths[i] > 0:
                    j = stack[-1]
                    
                    if healths[j] < healths[i]:
                        stack.pop()
                        healths[i] -= 1
                        healths[j] = 0
                    elif healths[j] > healths[i]:
                        healths[j] -= 1
                        healths[i] = 0
                        break
                    else:
                        stack.pop()
                        healths[i] = 0
                        healths[j] = 0
                        break
        
        # collect survivors
        res = []
        for i in range(n):
            if healths[i] > 0:
                res.append((robots[i][3], healths[i]))  # original index
        
        # sort by original index
        res.sort()
        
        return [h for _, h in res]