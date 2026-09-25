function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) {
      return false
    }

    const counts: Record<string, number>={}
    for (const ch of s) {
      counts[ch] = (counts[ch] || 0)+1
    }
    
    for (const ch of t) {
      if (!counts[ch]) {
        return false
      }
      counts[ch]--
    }

    return true
};


const text_s="dog a"
const text_t="goda"
const result = isAnagram(text_s, text_t )
console.log("Is anagram ? ", result)


// Analysis Complexity




// function isAnagram(s: string, t: string): boolean {
//   if (s.length !== t.length) return false;

//   // Int32Array creates a fixed block of memory initialized to 0s
//   const counts = new Int32Array(26);

//   for (let i = 0; i < s.length; i++) {
//     // Increment for s, decrement for t in a single loop!
//     counts[s.charCodeAt(i) - 97]++;
//     counts[t.charCodeAt(i) - 97]--;
//   }

//   // Check if any count is non-zero
//   for (let i = 0; i < 26; i++) {
//     if (counts[i] !== 0) return false;
//   }

//   return true;
// }

// 1. ⏱️ Time Complexity: $O(N)
// $Counting Loop: We iterate through strings $s$ and $t$ in a single loop. If $N$ is the length of the string, this loop runs $N$ times. Finding character codes (charCodeAt) and updating an array index are $O(1)$ constant-time operations.
// Verification Loop: The second loop checks the counts array, which always runs exactly 26 times, regardless of how long the input strings are. Since 26 is a constant, this takes $O(1)$ time.
// Total Time Complexity: $O(N)$ where $N$ is the length of the strings.


// 2. 🧠 Space Complexity: $O(1)
// $Memory Allocation: The Int32Array(26) creates a fixed block of memory (26 integers $\times$ 4 bytes = 104 bytes).
// Because the size of counts is fixed at 26 and does not grow as the input string length $N$ grows, the space required remains constant.
// Total Auxiliary Space Complexity: $O(1)$ constant space.