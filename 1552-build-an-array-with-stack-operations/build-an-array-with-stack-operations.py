class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stream = [i for i in range(1, n+1)]
        lst = set(target)
        stack = []
        for i in stream:
            stack.append("Push")
            if i not in lst:
                stack.append("Pop")
            if target[-1] == i:
               break
        return stack

        