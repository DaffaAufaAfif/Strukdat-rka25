# problem: https://leetcode.com/problems/baseball-game/?envType=problem-list-v2&envId=stack
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        li = []
        for i in operations:
            if i == '+':
                if len(li)>=2:
                    li.append((li[-1]+li[-2]))
            elif i == 'D':
                if len(li):
                    li.append((li[-1]*2))
            elif i == 'C':
                li.pop()
            else:
                li.append(int(i))
        return sum(li)

if __name__ == "__main__":
    sol = Solution()
    li = input().split()
    #li = ["5","2","C","D","+"]
    print(sol.calPoints(li))