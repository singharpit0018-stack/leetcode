class Solution {
public:
    int climbStairs(int n) {
        int curr=1,prev=1,prev1=1;
        for (int i=2;i<=n;i++){
            curr=prev+prev1;
            prev1=prev;
            prev=curr;
        }
        return curr;
        
    }
};