'''

class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {

        vector<int>Min;
        for(int i = 0;i < timePoints.size();i++){

            string curr = timePoints[i];

            // stoi -- > used for conver the string into the integer
            int hr = stoi(curr.substr(0,2));
            int mins = stoi(curr.substr(3,2));

            // convert all the time into the min

            int totalMinutes = hr*60 + mins;

            Min.push_back(totalMinutes);
        }


        sort(Min.begin(),Min.end());

        // find Diff
        int Minans = INT_MAX;
        int n = Min.size();
        for(int i = 0; i <n-1;i++){

            int diff = Min[i+1] - Min[i];
            Minans = min(Minans,diff);

        }

        // edge case


        int lastDiff =(Min[0] + 1440) - Min[n-1];
        Minans = min(Minans,lastDiff);
        return Minans;


    }
};
'''