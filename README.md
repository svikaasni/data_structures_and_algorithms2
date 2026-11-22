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
