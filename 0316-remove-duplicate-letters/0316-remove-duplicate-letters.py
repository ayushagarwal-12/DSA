class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}

        # Store last occurrence of each character
        for i in range(len(s)):
            last[s[i]] = i

        stack = []
        seen = set()

        for i, ch in enumerate(s):

            if ch in seen:
                continue

            while (
                stack
                and ch < stack[-1]
                and i < last[stack[-1]]
            ):
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)