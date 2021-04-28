class EmptyQueueError(Exception):
    pass
class Queue:
    def __init__(self):
        self.tems=[]

    def is_empty(self):
        return self.item==[]

    def size(self):
        return len(self.items)

    def enqueue(self.item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("queue is empty")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("queue is empty ")
        raise self.items[0]

class EmptyQueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.item=[]
        self.front=0

    def is_empty(self):
        return self.front==len(self.items)

    def size(self):
        return len(self.items)-self.front

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self,item):
        if self.is_empty():
            raise EmptyQueueError("queue is empty")

            x=self.items[self.front]
            self.items[self.front]=None
            self.front=self.front+1
            return x

    def peek(self):
        if self.is_empty():
            return EmptyQueueError("queue is empty")
        return self.items[self.front]

    def display(self):
        print(self.items)

    
### LINKED LIST IMPLEMENTATION  OF QUEUE ###

class EmptyQueueError(Exception):
    pass 

class Node:

    def __init__(self):
        self.front=None
        self.rear=None
        self.size_queue=0

    def is_empty(self):
        return self.front==None

    def size(self):
        return self.size_queue

    def enqueue(self,data):
        temp=Node(data)
        if self.front==None:
            self.front=temp
        else:
            self.rear.link=temp
        self.rear=temp
        self.size_queue+=1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("queue is empty")
        x=self.front.info 
        self.front=self.front.link



    





