class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedlist:

    def __init__(self):
        self.start=None

    def display_list(self):
        if self.start=None:
            print("list is empty")
            return 

        p=self.start
        while p is not None:
            print(p.data,"-->",end=" ")
            p=p.next

    def insert_in_beginning(self,data):
        temp=Node(data)
        temp.next=self.start
        self.start.prev=temp
        self.start=temp

    def insert_in_empty_list(self,data):
        temp=Node(data)
        self.start=temp

    def insert_at_end(self,data):
        temp=node(data)
        p=self.start
        while p.next is not None:
            p=p.next
        p.next=temp
        temp.prev=p
        
    def create_doubly_linkedlist(self):
        n=int(input("enter no  of leements to be inserted"))
        if n==0:
            return
        data=int(input("enter first element"))
        self.insert_in_empty_list(data)
        for i in range(n-1):
            data=int(input("enter next element"))
            self.insert_at_end(data)


    def insert_after_node(self,data,x):
        temp= Node(data)
        p=self.start
        while p is not None:
            if p.data==x:
                break
            p=p.next

        if p is None:
            printx(x," not present ") 
        else:
            temp.prev=p
            temp.next=p.next
             
            if p.next is not None:     #should not be done p is last node 
                p.next.pev=temp
            p.next=temp

    def insert_before(self,data,x):
        if self.start is None:
            print("list is empty")
            return
        if self.start.data==x:
            temp=Node(data)
            temp.next=self.start
            self.start.prev=temp
            self.start=temp
            return 
        p=self.start
        while p is not None:
            if p.data==x:
                break
            p=p.next
        if p is None:
            print(x,"not present in the list ")
        else:
            temp=Node(data)
            temp.prev=p.prev
            temp.next=p
            p.prev.next=temp
            p.prev=temp

    def delete_first_node(self):
        if self.start is None:                #list is empty
            return
        if self.start.next is None:           #list has only one node 
            self.start=None
            return 
        self.start=self.start.next 
        self.start.prev=None

    def delete_last_node(self):
        if self.start is None:               #list is empty
            return
        if self.start.next is None:
            self.start=None
            return
        p=self.start
        while p.next != None:
            p=p.next
        p.prev.next=None

    def delete_node(self,x):
        if self.start is None:
            return 
        if self.start.next is None:
            if self.start.data==x:
                self.start=None
            else:
                print(x,"not found")
            return

        #delete of first node 
        if self.start.data==x:
            self.start=self.start.next
            self.start.prev=None
            return

        p=self.start.next
        while p.next is not None:
            if p.data==x:
                break
            p=p.next

            


        
        










