// 1701. Average Waiting Time

class Solution {
public:
  double averageWaitingTime(vector<vector<int>>& customers) {
    double curr = customers[0][0];
    double wait = 0;
    
    for (auto c: customers) {
      if (curr < c[0]) {
        curr = c[0];
      }
      
      curr += c[1];
      wait += curr - c[0];
      // cout << c[0] << ',' << c[1] << endl;
    }
    
    return wait / double(customers.size());
  }
};