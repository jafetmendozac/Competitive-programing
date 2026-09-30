import java.util.HashMap;
import java.util.Map;

class Main {
  public static boolean isAnagram(String s, String t) {

    if (s.length() != t.length()) {
      return false;
    }

    Map<Character, Integer> result = new HashMap<>();
    for(char c : s.toCharArray()) {
      result.merge(c, 1, Integer::sum);
    }

    for(char c : t.toCharArray()){
      if( (result.getOrDefault(c, 0)) == 0 ) {
        return false;
      }
      result.put(c, result.get(c)-1);
    }

    return true;
  }

  public static void main(String[] args) {
    String text_s = "dog";
    String text_t = "dop";
    if (isAnagram(text_s, text_t)) {
      System.out.println("Las palabras: " + text_s + " y " + text_t + " son anagramas");
    } else {
      System.out.println("Las palabras no son anagramas");

    }
  }
}

// Time (average)	O(n)
// Time (worst)	O(n log n) or O(n²) (with bad hashing)
// Space	O(k) → O(n) worst, O(1) for fixed alphabet
// Passes over input	2



// if (s.length() != t.length()) return false;

// int[] count = new int[26];
// for (int i = 0; i < s.length(); i++) {
//     count[s.charAt(i) - 'a']++;
//     count[t.charAt(i) - 'a']--;
// }
// for (int c : count) if (c != 0) return false;
// return true;