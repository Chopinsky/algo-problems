// 219. Contains Duplicate II

class Solution {
public:
  bool containsNearbyDuplicate(vector<int>& nums, int k) {
    unordered_map<int, int> store;
    int val, dist;
      
    for (int i = 0; i < nums.size(); i++) {
      val = nums[i];
      auto last = store.find(val);
      
      if (last != store.end() and i - last->second <= k) {
        return true;
      }
      
      store[val] = i;
    }
    
    return false;
  } 
};