class BrowserHistory:

    def __init__(self, homepage: str):
        self.li = [homepage]
        self.buff = []

    def visit(self, url: str) -> None:
        self.li.append(url)
        self.buff.clear()
        #print(self.li)
    def back(self, steps: int) -> str:
        l = len(self.li)
        x = max(l-steps, 1)
        for i in range(l-x):
            if len(self.li) == 1:
                break
            temp=self.li.pop()
            self.buff.append(temp)
        print(steps,self.li,self.buff)
        return self.li[-1]
    def forward(self, steps: int) -> str:
        l = len(self.buff)
        x = max(l-steps, 0)
        for i in range(l-x):
            if len(self.buff) == 0:
                break
            temp=self.buff.pop()
            self.li.append(temp)
        return self.li[-1]
    def all(self):
        return self.li, self.buff
if __name__ == "__main__":
    bro = BrowserHistory("Nol")
    bro.visit("satu")
    bro.visit("dua")
    print(bro.back(1))
    bro.visit("tiga")
    print(bro.all())
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)