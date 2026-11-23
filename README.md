# LeetCode 49 – Group Anagrams

## Problem Statement
Given an array of strings `strs`, group all anagrams together. Anagrams are words that contain the same characters with the same frequency but may appear in a different order.

Return the grouped anagrams in any order.

## Approach: Hash Map + Sorting

The solution uses a dictionary to group words based on their sorted character representation.

1. Create an empty dictionary called `groups`.
2. Iterate through each word in the input list.
3. Sort the characters of the word alphabetically.
4. Use the sorted word as the dictionary key.
5. Append the original word to the corresponding group.
6. Return all dictionary values as a list.

## Python Solution

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
```

## Example 1

**Input:**
```python
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

**Output:**
```python
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

**Explanation:**

- `"eat"`, `"tea"`, and `"ate"` are anagrams.
- `"tan"` and `"nat"` are anagrams.
- `"bat"` forms a separate group.

## Example 2

**Input:**
```python
strs = [""]
```

**Output:**
```python
[[""]]
```

## Example 3

**Input:**
```python
strs = ["a"]
```

**Output:**
```python
[["a"]]
```

## Complexity Analysis

Let:
- `n` = Number of strings.
- `k` = Maximum length of a string.

- **Time Complexity:** O(n × k log k) – Each string is sorted before grouping.
- **Space Complexity:** O(n × k) – Stores the dictionary keys and grouped strings.

## Key Concepts
- Hash Maps (Dictionaries)
- String Manipulation
- Sorting
- Anagram Detection
- Grouping Elements

## LeetCode Details
- **Problem Number:** 49
- **Problem Name:** Group Anagrams
- **Difficulty:** Medium
- **Language:** Python
- **Topics:** Array, Hash Table, String, Sorting


---

# LeetCode 3331 – Find Subtree Sizes After Changes

## Problem Statement

You are given:
- An integer array `parent`, where `parent[i]` represents the parent of node `i` in a rooted tree.
- A string `s`, where `s[i]` represents the character assigned to node `i`.

For every node, find the nearest ancestor (excluding itself) having the same character. If such an ancestor exists, change the node's parent to that ancestor.

After performing all parent changes simultaneously, return an array `answer`, where `answer[i]` represents the size of the subtree rooted at node `i`.

## Approach: DFS + Hash Map + Tree Construction

The solution uses three main steps.

### 1. Build the Original Tree
- Create an adjacency list using the `parent` array.
- Store the children of each node.

### 2. Find the Nearest Matching Ancestor
- Perform an iterative DFS traversal.
- Maintain a dictionary called `last` to track the nearest ancestor for each character.
- If the current node has an ancestor with the same character, update its parent.
- Otherwise, retain its original parent.
- Restore the dictionary values during backtracking to maintain the correct ancestor information for different branches.

### 3. Calculate Subtree Sizes
- Construct a new tree using the updated parent relationships.
- Traverse the modified tree.
- Initialize every node's subtree size to `1`.
- Process nodes in reverse traversal order and add the sizes of their child subtrees.

## Python Solution

```python
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children


---

LeetCode 1352 – Product of the Last K Numbers

Difficulty: Medium
Topics: Array, Design, Prefix Product

Problem Description

Design a data structure that supports two operations:

- "add(num)": Adds an integer "num" to the stream.
- "getProduct(k)": Returns the product of the last "k" numbers in the stream.

If the last "k" numbers contain zero, return "0".

Approach: Prefix Product

Maintain an array of prefix products to calculate the product of the last "k" elements efficiently.

Algorithm

1. Initialize the prefix product array with "[1]".
2. When adding a number:
   - If the number is "0", reset the prefix array to "[1]".
   - Otherwise, multiply it by the previous prefix product and append the result.
3. When calculating the product of the last "k" numbers:
   - If "k >= len(prefix)", return "0" because the range contains a zero.
   - Otherwise, divide the latest prefix product by the prefix product before the last "k" elements.

Python Solution

class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0

        return self.prefix[-1] // self.prefix[-k-1]

Example

Input:

add(3)
add(0)
add(2)
add(5)
add(4)
getProduct(2)
getProduct(3)
getProduct(4)

Output:

20
40
0

Complexity Analysis

Operation| Time Complexity
"add(num)"| O(1)
"getProduct(k)"| O(1)

Space Complexity: O(n), where "n" is the number of elements stored since the most recent zero.

Key Learnings

- Understanding prefix products.
- Applying cumulative multiplication.
- Handling zero efficiently by resetting the prefix array.
- Optimizing range product queries to O(1) time.

Key Concept

The product of the last "k" elements can be calculated using:

[
Product = \frac{Prefix[n]}{Prefix[n-k]}
]

This approach avoids repeatedly multiplying the last "k" elements and provides an efficient solution.
