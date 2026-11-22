
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        last = {}
        new_parent = [-1] * n

        stack = [(0, 0, None, None)]

        while stack:
            node, state, char, old = stack.pop()

            if state == 1:
                if old is None:
                    del last[char]
                else:
                    last[char] = old
                continue

            c = s[node]
            old = last.get(c)

            new_parent[node] = old if old is not None else parent[node]

            last[c] = node

            stack.append((node, 1, c, old))

            for child in reversed(children[node]):
                stack.append((child, 0, None, None))

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        order = [0]

        for node in order:
            for child in new_children[node]:
                order.append(child)

        ans = [1] * n

        for node in reversed(order):
            for child in new_children[node]:
                ans[node] += ans[child]

        return ans
