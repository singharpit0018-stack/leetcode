class Solution {
public:
    bool isPalindrome(int n) {
    
        if (n < 0) return false;

        long long rev = 0;
        int rem = 0;
        int temp = n;

        while (n != 0) {
            rem = n % 10;
            rev = rev * 10 + rem;
            n /= 10;
        }

    
        return (rev == temp); 
    }
};