// 2337. Move Pieces to Obtain a String

class Solution {
public:
  bool canChange(string start, string target) {
    int i = 0, j = 0;
    int sl = start.size(), tl = target.size();
    
    if (sl != tl) {
      return false;
    }

    while (i < sl || j < tl) {
      while (i < sl && start[i] == '_') {
        i++;
      }

      while (j < tl && target[j] == '_') {
        j++;
      }

      // cout << start[i] << ',' << target[j] << endl;
      if (i >= sl && j >= tl) {
        return true;
      }
      
      if (i >= sl || j >= tl || start[i] != target[j]) {
        // cout << '1?' << endl;
        return false;
      }
      
      if ((start[i] == 'L' && i < j) || (start[i] == 'R' && i > j)) {
        // cout << '2?' << endl;
        return false;
      }

      i++;
      j++;
    }

    // cout << i << '-' << j << endl;
    return i >= sl && j >= tl;
  }
};