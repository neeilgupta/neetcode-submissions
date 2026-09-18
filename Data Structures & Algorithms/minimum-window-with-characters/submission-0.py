class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        lowest_size = float('inf')
        result = ""
        need_map = defaultdict(int)
        for char in t:
            need_map[char] += 1
        need = len(need_map)
        window_map = defaultdict(int)
        have = 0
        left = 0
        for right in range(len(s)):
            window_map[s[right]] += 1
            if window_map[s[right]] == need_map[s[right]]: 
                have += 1
            while have == need:
                current_size = right - left + 1
                if current_size < lowest_size:
                    lowest_size = current_size
                    result = s[left:right+1]
                window_map[s[left]] -= 1
                if window_map[s[left]] < need_map[s[left]]:
                    have -= 1
                left += 1
        return result