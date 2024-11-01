'''

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    long long kthLargestLevelSum(TreeNode* root, int k) {

        vector<long long>sums;
        queue<TreeNode*>q;
        q.push(root);
        while(q.size()>0){
            int l=q.size();
            long long sum=0;
            for(int i=0;i<l;i++){
                auto top=q.front();
                q.pop();
                sum+=top->val;
                if(top->left){
                    q.push(top->left);
                }
                if(top->right){
                    q.push(top->right);
                }
            }
            sums.push_back(sum);
        }
        sort(sums.begin(),sums.end());
        if(sums.size()<k)
        return -1;
        return sums[sums.size()-k];
    }
};

'''