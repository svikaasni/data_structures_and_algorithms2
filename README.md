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
