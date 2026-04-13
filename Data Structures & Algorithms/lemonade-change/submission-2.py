class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_count = defaultdict(int)
        for bill in bills:
            if bill == 5:
                bill_count[5] +=1
            elif bill == 10:
                if bill_count[5]>=1:
                    bill_count[5]-=1
                else:
                    return False
                bill_count[10] +=1
            else:
                if bill_count[10] >= 1 and bill_count[5] >= 1:
                    bill_count[10]-=1
                    bill_count[5]-=1
                elif bill_count[5] >= 3:
                    bill_count[5]-=3
                else:
                    return False
        
        return True