'''
class Solution
{
public:
    void helper(vector<int>& nums,int index,int tmp,int &sum)
    {
        if(index==nums.size())
        {
            sum+=tmp;
            return;
        }
        helper(nums,index+1,tmp^nums[index],sum);
        helper(nums,index+1,tmp,sum);
    }
    int subsetXORSum(vector<int>& nums)
    {
        int sum=0;
        helper(nums,0,0,sum);
        return sum;
    }
};

'''