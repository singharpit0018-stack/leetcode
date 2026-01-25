class Solution {
public:
    int romanToInt(string s) {
    
    int num = 0;
    map<char, int> m = {
        {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, 
        {'C', 100}, {'D', 500}, {'M', 1000}
    };

    for (int i = 0; i < s.length(); i++) {
        if (i + 1 < s.length() && m[s[i]] < m[s[i + 1]]) {
            num -= m[s[i]];
        } else {
            num += m[s[i]];
        }
    }
    return num;
}
        
        

};