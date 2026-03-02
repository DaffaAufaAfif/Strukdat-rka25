# problem: https://leetcode.com/problems/baseball-game/?envType=problem-list-v2&envId=stack
class Solution:
    def __init__(self):
        self.nums = 0
    def calPoints(self, operations: list[str]) -> int:
        li = []
        for i in operations:           
            if i == '+':
                if self.nums>=2:
                    satu = li.pop()
                    dua = li.pop()
                    print(li)
                    li.append(dua)
                    li.append(satu)
                    li.append((satu+dua))
                    self.nums+=1
            elif i == 'D':
                if self.nums!=0:
                    satu = li.pop()
                    li.append(satu)
                    li.append((satu*2))
                    self.nums+=1

            elif i == 'C':
                li.pop()
                self.nums-=1
            else:
                li.append(int(i))
                self.nums+=1
        sums = 0
        while li:
            sums += li.pop()
        return sums
    
if __name__ == "__main__":
    sol = Solution()
    li = input().split()
    #li = ["5","2","C","D","+"]
    print(sol.calPoints(li))