class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_set = set(target)
        data = []

        for i in range(1, n + 1):
            data.append("Push")

            if i not in target_set:
                data.append("Pop")

            if i == target[-1]:
                break

        return data