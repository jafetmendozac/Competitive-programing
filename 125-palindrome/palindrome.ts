function isPalindrome(s: string): boolean {
  const filtered: string[] = []

  for(const ch of s) {
    if (/^[a-z0-9]$/i.test(ch)) {
      filtered.push(ch.toLowerCase())
    }
  }

  const normalized = filtered.join("")
  let left = 0
  let right = normalized.length - 1
  while (left < right) {
    if (normalized[left] !== normalized[right]) {
      return false
    }
    left++
    right--
  }

  return true
};


const text = "«Anita: []  lava== la tina»"
console.log(`Is palindrome? ${isPalindrome(text)}`)

// Complexity Analysis

// Tiempo: O(n)
// Espacio: O(n)