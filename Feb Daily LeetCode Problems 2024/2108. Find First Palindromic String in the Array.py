'''

class Solution {
public:
    string firstPalindrome(vector<string>& words)
    {
        string x;
        int flag=0;
        for(int i=0;i<words.size();i++)
        {
            x=words[i];
            reverse(words[i].begin(),words[i].end());
            if(x==words[i])
            {
                flag=1;
                break;
            }
        }
        return flag==0?"":x;

    }
};

'''