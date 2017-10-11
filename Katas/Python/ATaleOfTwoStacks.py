
class MyQueue(object):
    foo = []
    bar = []
    #def peek(self):

    #def pop(self):

    def put(self, value):
        self.bar = self.foo
        self.foo.append(value)
        for item in self.bar:
            self.foo.append(self.bar.pop())

queue = MyQueue()

t = int(input())

for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())