class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_set = set(target)
        Stack = []

        for i in range(1, n + 1):
            Stack.append("Push")

            if i not in target_set:
                Stack.append("Pop")

            if i == target[-1]:
                break

        return Stack