import sys
from collections import deque 

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class teque():

    def __init__(self):
        self.head = None
        self.tail = None
        self.middle = None
        self.len = 0

    def push_front(self,new_data):
        self.len += 1
        new_node = Node(new_data)
        new_node.next = self.head            

        if self.len > 1:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
        else:
            self.head = new_node
            self.tail = new_node
            self.middle = new_node
            new_node.prev = None

        if self.len % 2 and self.len > 1:
                self.middle = self.middle.prev


    def push_back(self,new_data):
        self.len +=1
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.len > 1:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        else:
            self.head = new_node
            self.tail = new_node
            self.middle = new_node
            new_node.next = None
        
        if not self.len % 2 and self.len > 1:
                self.middle = self.middle.next
    
    def push_middle(self,new_data):
        self.len +=1
        new_node = Node(new_data)

        if self.len > 2:

            if self.len % 2:
                new_node.prev = self.middle.prev
                new_node.next = self.middle

                self.middle.prev.next = new_node
                self.middle.prev = new_node
                self.middle = new_node
            else:
                new_node.prev = self.middle
                new_node.next = self.middle.next

                self.middle.next.prev = new_node
                self.middle.next = new_node
                self.middle = new_node

        else:
            self.len -=1
            self.push_front(new_data)


    def get(self,index):
        if index >= self.len:
            return(0/0)
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            return(curr.data)
    
    def show(self):
        curr = self.head
        out = []
        for i in range(self.len):
            out.append(curr.data)
            curr = curr.next
        print(out,self.head.data,self.middle.data,self.tail.data)


ins = -1
innr = 0
for line in sys.stdin:
    if innr == 0:
        ins = int(line.strip())
        q = teque()
    else:
        com, num = line.split()
        num = int(num)
        if com == "push_back":
            q.push_back(num)
        elif com == "push_middle":
            q.push_middle(num)
        elif com == "push_front":
            q.push_front(num)
        else:
           print(q.get(num))
        #q.show()
    if innr == ins:
        break
    innr +=1
