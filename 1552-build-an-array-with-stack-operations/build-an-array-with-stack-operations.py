class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_set = set(target)
        s = []

        for i in range(1, n + 1):
            s.append("Push")

            if i not in target_set:
                s.append("Pop")

            if i == target[-1]:
                break

        return s