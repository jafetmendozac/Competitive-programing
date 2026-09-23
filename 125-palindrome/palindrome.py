class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered=""
        for ch in s:
            if ch.isalnum():
                filtered = filtered + ch.lower()
        
        right = len(filtered) - 1
        left = 0
        while left < right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1

        return True


sol = Solution()
text = "«Anita: []  lava== la tina»"
result = sol.isPalindrome(text)

print(f"Is palindrome? {result}")


# Complexity Analysis
# Time Complexity: O(n), where n is the length of the input string s. We iterate through the string once to filter out non-alphanumeric characters and convert to lowercase, and then we perform a two-pointer check which also takes O(n) time in the worst case.
# Space Complexity : O(n), where n is the length of the filtered string. We create a new string to store the filtered characters, which can take up to O(n) space in the worst case.