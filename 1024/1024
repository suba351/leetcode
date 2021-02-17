class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if T == 0:
            return 0
        clips.sort()
        print(clips)
        n = len(clips)
        next_el = [-1] * n
        i = 0
        while i < n - 1:
            j = i + 1
            right = clips[j][1]
            while clips[i][1] >= clips[j][0]:
                if right <= clips[j][1]:
                    right = clips[j][1]
                    next_el[i] = j
                j += 1
                if j > n - 1: break
            i += 1
        ans = float('inf')
        print(next_el)
        i = 0
        while clips[i][0] == 0 and i < n - 1:
            l = i
            r = i
            cost = 1
            T_curr = clips[r][1] - clips[l][0]
            if T_curr >= T:
                    ans = min(ans, cost)
            while next_el[r] != -1 and r < n - 1:
                r = next_el[r]
                T_curr = clips[r][1] - clips[l][0]
                cost += 1
                if T_curr >= T:
                    ans = min(ans, cost)
                    r = n - 1
            i += 1
        if ans == float('inf'):
            return -1
        else:
            return ans
