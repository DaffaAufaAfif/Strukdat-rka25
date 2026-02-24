class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        li = []
        for i in tokens:
            l = len(li)
            a = i
            if i == '+':
                if l >1:
                    a = li[-1]
                    li.pop()
                    a += li[-1]
                    li.pop()
                else:
                    continue
            elif i == '-':
                if l >1:
                    a = li[-2]
                    a -= li[-1]
                    li.pop()
                    li.pop()
                else:
                    continue
            elif i == '*':
                if l >1:
                    a = li[-1]
                    li.pop()
                    a *= li[-1]
                    li.pop()
                else:
                    continue
            elif i == '/':
                if l >1:
                    a = li[-2]
                    a /= li[-1]
                    li.pop()
                    li.pop()
                else:
                    continue
            li.append(int(a))
        return int(sum(li))

if __name__ == "__main__":
    sol = Solution()
    i = input().split()
    print(sol.evalRPN(i))