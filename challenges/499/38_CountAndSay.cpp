class Solution {
public:
  string countAndSay(int n) {
    int idx = 1;
    string s = "1";
  
    while (idx < n) {
      string nxt;
      string last;
      int count = 0;
        
      for (int i = 0; i < s.size(); i++) {
        string ch(1, s[i]);
        
        if (ch == last) {
          count++;
        } else {
          if (count > 0) {
            nxt += to_string(count) + last;
          }
          
          last = ch;
          count = 1;
        }
      }
      
      if (count > 0) {
        nxt += to_string(count) + last;
      }
      
      s = nxt;
      idx++;
    }
  
    return s;
  }
};