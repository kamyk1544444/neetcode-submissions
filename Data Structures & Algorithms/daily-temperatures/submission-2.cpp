class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        
        int n = temperatures.size();

        stack<pair<int,int>> stacker;

        vector<int> wynik(n,0);

        for(int i=0; i<n; ++i){

            while(!stacker.empty() && stacker.top().first < temperatures[i]){
                int si = stacker.top().second; int st = stacker.top().first;
                stacker.pop();

                wynik[si] = i -si;
            }
            stacker.push({temperatures[i],i});

        }
        return wynik;



    }
};
