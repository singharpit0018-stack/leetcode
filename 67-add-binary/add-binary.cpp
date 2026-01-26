class Solution {
public:
    string addBinary(string a, string b) {
        
        if (a.length() > b.length()) {
            int numLeadingZeros = a.length() - b.length();
            b.insert(0, numLeadingZeros, '0');
        } else if (b.length() > a.length()) {
            int numLeadingZeros = b.length() - a.length();
            a.insert(0, numLeadingZeros, '0');
        }

        string sum = "";
        int carry = 0;

        
        for (int i = a.length() - 1; i >= 0; i--) {
            int digit1 = a[i] - '0';
            int digit2 = b[i] - '0';
            int d = 0;
            if (digit1 == 0 && digit2 == 0) {
                if (carry == 0) {
                    d = 0; carry = 0;
                } else {
                    d = 1; carry = 0;
                }
            } else if (digit1 == 0 && digit2 == 1) {
                if (carry == 0) {
                    d = 1; carry = 0;
                } else {
                    d = 0; carry = 1;
                }
            } else if (digit1 == 1 && digit2 == 0) {
                if (carry == 0) {
                    d = 1; carry = 0;
                } else {
                    d = 0; carry = 1;
                }
            } else if (digit1 == 1 && digit2 == 1) {
                if (carry == 0) {
                    d = 0; carry = 1;
                } else {
                    d = 1; carry = 1;
                }
            }
            sum.insert(0, 1, (char)('0' + d));
        }

        if (carry == 1) {
            sum.insert(0, 1, '1');
        }

        return sum;
    }
};