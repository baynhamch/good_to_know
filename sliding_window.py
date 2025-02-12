"""
The Sliding Window technique is a way to efficiently process problems that involve subarrays or substrings by moving two pointers (left and right) dynamically instead of checking all possible substrings (which would be slow).
"""



def lengthOfLongestSubstring(s):
    char_set = set()  # HashSet to store unique characters
    l = 0  # Left pointer
    max_length = 0  # To store the max length of unique substring

    for r in range(len(s)):  # Right pointer moves through s
        while s[r] in char_set:  # If duplicate found
            char_set.remove(s[l])  # Remove leftmost character
            l += 1  # Move left pointer right
        
        char_set.add(s[r])  # Add the new character to the set
        max_length = max(max_length, r - l + 1)  # Update max length

    return max_length
