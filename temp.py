
from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:        
        update_list = people[:]

        ret = []
        for i in range(len(people)):
            min_ = min([x for x, before in update_list if before == 0])
            ret.append([min_, 0])
            for index, (height, infront) in enumerate(update_list):
                if height <= min_:
                    update_list[index][1] -= 1
        
        # now refigure out the original order in the queue
        for i in range(1, len(update_list)):
            for j in range(i):
                if ret[j] >= ret[i]:
                    ret[i][1] += 1
        return ret
    
Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])