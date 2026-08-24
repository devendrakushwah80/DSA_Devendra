class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        st = []
        ans=[]
        for i in range(len(intervals)):
            st.append([intervals[i][0],i])
        st.sort()

        for i in range(len(intervals)):
            target = intervals[i][1]

            l=0
            h=len(st)-1

            while l<=h:
                mid=(l+h)//2

                if st[mid][0]<target:
                    l=mid+1
                else:
                    h=mid-1
            if l == len(st):
                ans.append(-1)
            else:
                ans.append(st[l][1])
        return ans
