class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        h = len(people)-1
        count = 0
        while l<h:
            Sum = people[l]+people[h]
            if Sum <= limit:
                count+=1
                l+=1
                h-=1
            else:
                h-=1
                count+=1
        if l == h:
            count += 1
        return count
