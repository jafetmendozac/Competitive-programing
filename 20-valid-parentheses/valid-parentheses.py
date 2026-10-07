class Solution:
  def isValid(self, s: str) -> bool:

    pila=[]
    pares = {')': '(', ']': '[', '}': '{'}

    for char in s: 
      if char in '([{':
        pila.append(char)
      else:
        if not pila or pila[-1] != pares[char]:
          return False
        pila.pop()

    return True

sol = Solution()
text_1="()[]{}"
text_2="()" # v/
text_3="())" # v/
text_4="([])"
text_5="([)]"

sol.isValid(text_1)
sol.isValid(text_2)
sol.isValid(text_3)
sol.isValid(text_4)
sol.isValid(text_5)
