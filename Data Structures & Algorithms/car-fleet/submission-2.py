class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for p, s in zip(position, speed):
            current = (p, s)
            pair.append(current)
        pair.sort(reverse=True)
        stack = []
        for p, s in  pair:
            time_to_dest = (target - p) / s
            stack.append(time_to_dest)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        