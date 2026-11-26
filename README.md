s# LeetCode 49 – Group Anagrams

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

---


LeetCode 3411 – Maximum Subarray With Equal Products

Problem

Given an integer array "nums", find the maximum length of a contiguous subarray where the product of all elements is equal to the product of the GCD and LCM of all elements.

Approach: Brute Force

1. Initialize "ans = 0" to store the maximum valid subarray length.
2. Iterate through the array using index "i" as the starting point.
3. Initialize:
   - "prod = 1" – product of elements.
   - "g = 0" – GCD of elements.
   - "l = 1" – LCM of elements.
4. Extend the subarray using index "j".
5. Update the product, GCD and LCM for every new element.
6. Check whether "prod == g * l".
7. If the condition is satisfied, update the maximum length.
8. Return the maximum length.

Python Code

from math import gcd, lcm

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            g = 0
            l = 1

            for j in range(i, n):
                prod *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])

                if prod == g * l:
                    ans = max(ans, j - i + 1)

        return ans

Complexity Analysis

- Time Complexity: O(n² × log M), where "n" is the array length and "M" is the maximum element.
- Space Complexity: O(1), as only a constant number of variables are used.

Key Concepts

- Arrays
- Brute Force
- Nested Loops
- GCD (Greatest Common Divisor)
- LCM (Least Common Multiple)
- Subarrays

Key Learning

This problem demonstrates how to explore all contiguous subarrays while maintaining their product, GCD and LCM incrementally instead of recalculating them from scratch.


---


LeetCode 3934 – Smallest Unique Subarray

Problem

Find the minimum length of a subarray that occurs exactly once in the given array.

Approach

Binary Search + Sliding Window + Double Rolling Hash

1. Binary Search: Search for the minimum valid subarray length.
2. Sliding Window: Generate all contiguous subarrays of a fixed length efficiently.
3. Rolling Hash: Calculate and update hash values without repeatedly processing entire subarrays.
4. Frequency Map: Store the frequency of each subarray hash and check whether any subarray occurs exactly once.
5. If a unique subarray exists, search for a smaller length; otherwise, search for a larger length.

Python Solution

- Uses two independent hash functions to reduce collision probability.
- Updates window hashes in constant time.
- Uses a dictionary to track subarray frequencies.

Complexity Analysis

- Time Complexity: O(n log n)
- Space Complexity: O(n)

Where "n" is the length of the input array.

Key Concepts

- Binary Search on Answer
- Sliding Window
- Rolling Hash
- Hash Maps
- Subarray Frequency Counting

Learning Outcome

This problem demonstrates how binary search can optimize minimum-length problems when validity is monotonic. Combining sliding windows and rolling hashes allows efficient comparison of contiguous subarrays.


---

LeetCode 3360 – Stone Removal Game

Problem Description

Alice and Bob play a game starting with "n" stones.

- Alice starts by removing 10 stones.
- Bob removes 9 stones.
- Alice removes 8 stones.
- Bob removes 7 stones.
- The number of stones to remove decreases by 1 after every turn.
- A player loses if they cannot remove the required number of stones.

The task is to determine whether Alice wins.

Approach: Simulation

1. Initialize "turn = 10", representing the first number of stones Alice must remove.
2. Check whether the remaining stones are sufficient for the current turn.
3. If sufficient, subtract the required stones.
4. Decrease "turn" by 1 after every successful move.
5. Continue until a player cannot make their move.
6. Determine the winner based on whose turn it is.

Python Solution

class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn = 10

        while n >= turn:
            n -= turn
            turn -= 1

        return turn % 2 == 1

Example

Input:

n = 12

Output:

True

Explanation:

- Alice removes 10 stones. Remaining = 2.
- Bob needs to remove 9 stones but only 2 remain.
- Bob cannot make the move, so Alice wins.

Complexity Analysis

- Time Complexity: O(1) – At most 10 iterations.
- Space Complexity: O(1) – Uses only constant extra space.

Key Concepts

- Simulation
- While Loop
- Alternating Turns
- Conditional Logic

Learning Outcome

This problem demonstrates how to simulate a turn-based game using a loop and track alternating player turns to determine the winner.
