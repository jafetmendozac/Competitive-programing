class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

      if len(s) != len(t):
         return False

      counts ={}

      for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

      for ch in t:
        if counts.get(ch,0) == 0:
          return False
        counts[ch]-=1
      
      return True


sol = Solution()
text_s="ana"
text_t="god"
result = sol.isAnagram(text_s, text_t)
print(f"Is anagram? {result}")

#Analysis Complex
# Time	O(n)
# Space	O(k) — or O(1)