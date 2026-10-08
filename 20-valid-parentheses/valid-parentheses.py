class Solution:
  def isValid(self, s: str) -> bool:
    if len(s) % 2 == 1:
      return False

    pila = []
    pares = {')': '(', ']': '[', '}': '{'}

    for char in s:
      if char in '([{':
        pila.append(char)
      elif char not in pares or not pila or pila.pop() != pares[char]:
        return False

    return not pila

sol = Solution()
# text_1="()[]{}"
# text_2="()" # v/
# text_3="())" # v/
# text_4="([])"
# text_5="([)]"
text_6="(("

# sol.isValid(text_1)
# sol.isValid(text_2)
# sol.isValid(text_3)
# sol.isValid(text_4)
# sol.isValid(text_5)
print(sol.isValid(text_6))
