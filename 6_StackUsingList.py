class Stack:
    stack_lst=[]
    def push(self,element):
        self.stack_lst.append(element)
    def pop(self):
        temp = self.stack_lst[-1]
        del self.stack_lst[-1]
        return temp
    def peek(self):
        return self.stack_lst[-1]
    def is_empty(self):
        return len(self.stack_lst)==0

a=Stack()
a.push(5)
a.push(4)
a.push(8)
a.push(110)
print(a.pop())
print(a.pop())
print(a.peek())
