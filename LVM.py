class Lombok:
    def __init__(self):
        self.stack = []
        self.register = 0
    def push(self, n):
        self.stack.append(n)
    def store(self):
        if self.stack:
            self.register = self.stack.pop()
    def load(self):
        self.stack.append(self.register)
    def plus(self):
        if len(self.stack)>1:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a+b)
    def times(self):
        if len(self.stack)>1:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a*b)
    def done(self):
        if self.stack:
            print(self.stack[-1])
n = int(input())
commands = [input().split(' ') for _ in range(n)]
lvm = Lombok()    
i = 0
while i < n:
    cmd = commands[i]
    c = cmd[0].lower()

    if c== 'push':
        lvm.push(int(cmd[1]))
    elif c == 'store':
        lvm.store()
    elif c== 'load':
        lvm.load()
    elif c == 'plus':
        lvm.plus()
    elif c == 'times':
        lvm.times()
    elif c =='done':
        lvm.done()
    elif c == 'ifzero':
        if lvm.stack:
            val = lvm.stack.pop()
            if val == 0:
                i = int(cmd[1])
                continue
            
    i += 1   