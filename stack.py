class EmptyStackError:
    pass

class Stack:
    def __init__(self)
    self.items=[]

    def is_empty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

    def push(self,data):
        self.data.append(data)

    def pop(self):
        if self.is_empty():
            return EmptyStackError("stack is empty ")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("stack is empty")
        return self.items[-1]
    
    def display(self):
        print(self.items)


###################################

class stackEmpltyError(Exception):
    pass
class StackFullError(Exception):
    pass

class Stack:

    def __init__(self,max_size=10):
        self.data=[None]*max_size
        self.count=0

    def size(self):
        return self.count

    def is_empty(self):
        return self.count==0

    def is_full(self):
        return self.count==len(self.data)

    def push(self,x):
        if self.is_full():
            raise StackFullError("stack is full ,can't push ")

        self.data[self.count]=x
        self.count+=1


    def pop(self):
        if self.is_empty():
            raise stackEmpltyError("stack is empty,can't pop")

        x=self.items[self.count-1]
        self.data[self.count-1]=None
        self.count-=1
        return x

### LINKED LIST IMPLEMENTATION OF STACK ###


class EmptyStackError(Exception):
    pass

class Node:
    def __init__(self,value):
        self.info=value
        self.link=None

class stack:

    def __init__(self):
        self.top=None

    def is_empty(self):
        return self.top==None

    def size(self):
        if self.is_empty():
            return 0

        count=0
        p=self.top 
        while p is not None:
            count+=1
            p=p.link
        return count

    def push(self,data):
        temp=node(data)
        temp=link=self.top
        self.top=temp

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("stack is empty")
        popped=self.top.info 
        self.top=self.top.link
        return popped 

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("stack is empty")
        return self.top.info 

    def display(self):
        if self.is_empty():
            print("stack is empty")
            return
        print("stack is :")
        p=self.top 
        while p is not Node:
            print(p.info,"")
            p=p.link










    
    




    


    



