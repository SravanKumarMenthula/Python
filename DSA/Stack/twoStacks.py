class twoStacks:
    def __init__(self, size):
        self.size = size
        self.arr = [None]*size
        self.top1 = -1
        self.top2 = size

    def push1(self,data):
        if self.top1 < self.top2-1:
            self.arr[self.top1+1] = data
            self.top1 = self.top1 +1
        else:
            print("Stack Over flow")

    def push2(self, data):
        if self.top1 < self.top2 -1:
            self.arr[self.top2-1] = data
            self.top2 = self.top2 -1
        else:
            print("Stack Over flow")

    def pop1(self):
        if self.top1 > -1:
            x = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 = self.top1 - 1
            return x
        else:
            print("Under Flow")

    def pop2(self):
        if self.top2 < self.size:
            y = self.arr[self.top2]
            self.arr[self.top2] = None
            self.top2 = self.top2 + 1
            return y
        else:
            print("Under Flow")

    def printTwoStacks(self):
        for i in self.arr:
            print(i)

if __name__ == '__main__':
    ts = twoStacks(5)
    ts.push1(23)
    ts.push2(43)
    ts.push2(67)
    ts.push1(24)
    ts.printTwoStacks()
    print("Poping from 1:"+str(ts.pop1()))
    print("Poping from 2:"+str(ts.pop2()))
    ts.printTwoStacks()
