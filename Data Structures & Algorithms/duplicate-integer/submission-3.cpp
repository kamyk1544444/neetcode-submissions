class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        if(nums.size() <= 1)
            return false;
        sort(nums.begin(),nums.end());

        for(int i=0; i<nums.size(); ++i){
            if(nums[i] == nums[i+1]){
                return true;
            }
            if(i==nums.size()-2)
                return false;
        }
        

    }
};