class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

      unordered_map<string, vector<string>> tak;

      for(auto& wynik : strs){
        string srt= wynik;
        sort(srt.begin(),srt.end());
        tak[srt].push_back(wynik);
      }

      vector<vector<string>> final;

      for(auto& dawaj: tak){
        final.push_back(dawaj.second);
      }

      return final;
    }
};
