'''
1277. Count Square Submatrices with All Ones
'''

class Solution {
public:
  // the idea is that we can expand 1 more square to (i, j), from the min-side
  // from (i-1, j), (i, j-1), and (i-1, j-1)
  int countSquares(vector<vector<int>>& matrix) {
    int m = matrix.size();
    int n = matrix[0].size();
    int cnt = 0;
    
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (i > 0 and j > 0 and matrix[i][j] == 1) {
          matrix[i][j] = 1 + min(min(matrix[i-1][j], matrix[i][j-1]), matrix[i-1][j-1]);
        }
        
        cnt += matrix[i][j];
      }
    }
    
    return cnt;
  }
  
    
  int countSquares0(vector<vector<int>>& matrix) {
    int total = 0;
    const int m = matrix.size();
    const int n = matrix[0].size();
    std::vector<std::vector<int>> prefix(m, std::vector<int> (n, 0));
    
    auto count_ones = [&] (int x, int y, int side) {
      // cout << x << ", " << y << ", " << side << endl;
      if (matrix[x][y] == 0 || x+1 < side || y+1 < side) {
        return 0;
      }
      
      if (x+1 == side && y+1 == side) {
        return prefix[x][y];
      }
      
      if (x+1 == side) {
        return prefix[x][y] - prefix[x][y-side];
      }
      
      if (y+1 == side) {
        return prefix[x][y] - prefix[x-side][y];
      }
      
      return prefix[x][y] - prefix[x-side][y] - prefix[x][y-side] + prefix[x-side][y-side];
    };
    
    for (int i = 0; i < m; i++) {
      int row = 0;
      for (int j = 0; j < n; j++) {
        row += matrix[i][j];
        if (i == 0) {
          prefix[i][j] = row;
        } else {
          prefix[i][j] = row + prefix[i-1][j];
        }
        
        int side = 1;
        int bound = 1 + (i > j ? j : i);
        
        while (side <= bound) {
          int cnt = count_ones(i, j, side);
          // cout << "result:" << cnt << ", " << prefix[i][j] << endl;
          
          if (cnt < side * side) {
            break;
          }
          
          total++;
          side++;
        }
      }
    }
    
    return total;
  }
};