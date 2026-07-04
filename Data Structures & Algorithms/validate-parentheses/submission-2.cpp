class Solution {
public:
    bool isValid(string s) {
        stack<char> stacker;

        unordered_map<char,char> sizer = {
            {')','('},
            {'}','{'},
            {']','['}
        }  ;

        for(auto& znak: s){

            if(sizer.count(znak)){
                if(!stacker.empty() && stacker.top() == sizer[znak]){
                    stacker.pop();
                }
                else{
                    return false;
                }
            }
            else{
                stacker.push(znak);
            }

        }
        
        return stacker.empty();
    }
};
