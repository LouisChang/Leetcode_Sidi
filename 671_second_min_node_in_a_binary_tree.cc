/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int findSecondMinimumValue(TreeNode* root) {
        deque <TreeNode*> li;
        vector <int> res;
        li.push_back(root);
        res.push_back(root -> val);
        while (!li.empty()){
            TreeNode * node = li.front();
            li.pop_front();
            if ( node -> left){   li.push_back(node -> left); res.push_back(li.back() -> val);}
            if ( node -> right){   li.push_back(node -> right); res.push_back(li.back() -> val);}
        }
        set <int> s(res.begin(),res.end());
        if (s.size() <= 1){ return -1;} else {auto a = s.begin(); return *++a;}
    }
};
