class Solution {
    public boolean isPalindrome(String s) {
      StringBuilder sb = new StringBuilder();

      for(char ch: s.toCharArray()){
        if(Character.isLetterOrDigit(ch)) {
          sb.append(Character.toLowerCase(ch));
        }
      }

      int left=0;
      int right= sb.length()-1;

      while (left < right) {
        if (sb.charAt(left) != sb.charAt(right) ) {
          return false;
        }
        left += 1;
        right -=1;
      }

      return true;
    }
}

class Main {
  public static void main(String[] args) {
    Solution sol = new Solution();
    String text = "«Anita: []  lava== la tina»";
    System.out.println(sol.isPalindrome(text));
  }
}


// Time:  O(n)
// Space: O(n)