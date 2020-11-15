class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10 and five > 0:
                ten += 1
                five -= 1
            elif i == 20 and ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif i == 20 and five >= 3:
                five -= 3
            else:
                return False
        return True