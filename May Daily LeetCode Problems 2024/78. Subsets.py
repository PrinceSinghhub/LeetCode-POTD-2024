class Solution:

    def printAllSubsecquances(self,index,arr,myans,ans):

        if index >= len(arr):
            ans.append(myans[:])
            return

        myans.append(arr[index])
        self.printAllSubsecquances(index+1,arr,myans,ans)
        myans.remove(arr[index])
        self.printAllSubsecquances(index+1,arr,myans,ans)

    def subsets(self, arr):

        ans = []
        self.printAllSubsecquances(0,arr,[],ans)
        ans.sort()
        return ans
    