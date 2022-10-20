/** 
 *
 * 817. Linked List Components
 *
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
  int numComponents(ListNode* head, vector<int>& nums) {
    unordered_set<int> vals(nums.begin(), nums.end());
    int count = 0;
    bool chain = false;
        
    while (head) {
      // cout << head->val << endl;
      if (vals.find(head->val) != vals.end()) {
        if (!chain) {
          chain = true;
          count++;
        } 
      } else {
        chain = false;
      }
      
      head = head->next;
    }
    
    return count;
  }
};