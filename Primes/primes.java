// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Main {
    
    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for(int i = 3; i*i <= n; i+=2) {
           if(n % i == 0 ) {
               return false;
           }
        }
        return true;
    }
    
    public static void main(String[] args) {
        if(isPrime(5)) {
            System.out.println("Is prime");
        } else {
            System.out.println("Not is prime");
        }
    }
}