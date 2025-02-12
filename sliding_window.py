"""
The Sliding Window technique is a way to efficiently process problems that involve subarrays or substrings 
by moving two pointers (left and right) dynamically instead of checking all possible substrings 
(which would be slow).

Used in this problem
1.	A HashSet to store characters in the current substring.
2.	Two pointers (l and r) to define a “window” in the string.
3.	Expanding the window (r++) when there are no duplicates.
4.	Shrinking the window (l++) when a duplicate is found.
"""



def slidngWindow(s):
    seen = set()  # Store unique characters
    left = 0  # Left pointer
    max_length = 0  # Keep track of max substring length

    for right in range(len(s)):  # Right pointer moves through the string
        while s[right] in seen:  # If duplicate found, shrink window
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])  # Add current character
        max_length = max(max_length, right - left + 1)  # Update max length

    return max_length
