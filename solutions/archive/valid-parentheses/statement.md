# 20. Valid Parentheses

**Easy** · Stack · [problem on LeetCode](https://leetcode.com/problems/valid-parentheses/)
Fluency target: 15 min (prior)

---

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

	
- Open brackets must be closed by the same type of brackets.

	
- Open brackets must be closed in the correct order.

	
- Every close bracket has a corresponding open bracket of the same type.

 

**Example 1:**

**Input:** s = "()"

**Output:** true

**Example 2:**

**Input:** s = "()[]{}"

**Output:** true

**Example 3:**

**Input:** s = "(]"

**Output:** false

**Example 4:**

**Input:** s = "([])"

**Output:** true

**Example 5:**

**Input:** s = "([)]"

**Output:** false

 

**Constraints:**

	
- `1 <= s.length <= 10^4`

	
- `s` consists of parentheses only `'()[]{}'`.

---

*The examples above are pre-loaded into `TESTS` in the solution file —
`grind check` runs a few, `grind done` runs all of them and grades.*
