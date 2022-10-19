// 2087. Minimum Cost Homecoming of a Robot in a Grid

class Solution {
public:
  int minCost(vector<int>& startPos, vector<int>& homePos, vector<int>& rowCosts, vector<int>& colCosts) {
    int x0 = startPos[0];
    int y0 = startPos[1];
    int x1 = homePos[0];
    int y1 = homePos[1];
    
    if (x0 == x1 && y0 == y1) {
      return 0;
    }
    
    int hor=0, ver=0;
    for (int i = min(y0, y1); i <= max(y0, y1); i++) {
      hor += colCosts[i];
    }
    
    for (int i = min(x0, x1); i <= max(x0, x1); i++) {
      ver += rowCosts[i];
    }
    
    return (hor-colCosts[y0]) + (ver-rowCosts[x0]);
  }
};