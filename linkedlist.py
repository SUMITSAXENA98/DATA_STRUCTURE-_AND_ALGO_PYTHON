class Node:

    def __init__(self,data):
        self.data=data
        self.next=None



class SinglyLinkedList:

    def __init__(self):
        self.start=None

    def display_list(self):
        if self.start is None:
            print("list is empty")
            return

        else:
            print("list is :")
            p=self.start
            while p is not None:
                print(p.data," ",end=" ")
                p=p.next    

    def count_node(self):
        p=self.start
        n=0
        while p is not None:
            n=n+1
            p=p.next
        print("number of nodes ",n )


    def search(self,x):
        position=1
        p=self.start
        while p is not None:
            if p.data==x:
                print(x,"is at position",position)
                return True
            position=position+1
            p=p.next
        else:
            print(x,"not found in list ")
            return False
    def insert_in_beginning(self,data):
        temp=node(data)
        temp.next=self.start
        self.start=temp

    def insert_at_end(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
        else:
            p=self.start
            while p.next is not None:
                p=p.next
            p.next=temp

    def create_list(self):
        n=int(input("enter no of elements:"))
        if n==0:
            return
        for i in range(n):
            data=int(input("enetr element to be inserted :"))
            self.insert_at_end(data)



    def insert_after(self,data,x):
        p=self.start
        if p is None:
            print(x,"is not present")
        while p is not None:
            p=p.next
            if p.data==x:
                break
        temp=node(data)
        temp.next=p.next
        p.next=temp



    def insert_before(self,data,x):
        if self.start is None:
            print("list is empty")
            return
        
        if x==self.start:
            temp=Node(data)
            temp.next=self.start
            self.start=temp
            return
        
        p=self.start
        while p.next is not None:
            if p.next.next==x:
                break
            p=p.next

            if p.next is None:
                print(x,"not present in list")
            else:
                temp=Node(data)
                temp.next=p.next
                p.next=temp



    def insert_at_position(self,data,k):
        if k==1:
            temp=Node(data)
            temp.next=self.start
            self.start=temp
            return

        p=p.next
        i=1

        while i<k-1 and p is not None:
            p=p.next
            i=i+1

        if p is None:
            print("you can insert only at position ",i)

        else:
            temmp=Node(data)
            temp.next=p.next
            p.next=temp

    

    def delete_first_node(self):
        if self.start is None:
            return
        self.start=self.start.next

    def delete_last_node(self):
        if self.start is None:
            return
        if self.start.next is none:
            self.start=None
            return

        p=self.start
        while p.next.next is None:
            p=p.next 
        p.next=None

    def delete_node(self,x):
        if self.start is None:
            print("list is empty")
            return 

        if self.start.data==x:
            self.start=self.start.next 
            return
        
        p=self.start
        while p.next is not None:
            if p.next.data==x:
                break
            p=p.next

        if p.next is None:
            print("element",x,"not in list")
        else:
            p.next=p.next.next
            
    def has_cycle(self):
        if self.find_cycle() is None:
            return False
        else:
            return True


    def find_cycle(self):
        if self.start is None or self.start.link is None:
            return None
        slowR=self.start
        fastR=self.start
        while fastR is not None and fastR.link is not None:
            slowR=slowR.link
            fastR=fastR.link
            if slowR==fastR:
                 return slowR
        return None

    def remove_cycle(self):
        c=self.find_cycle()
        if c is None:
            return
        print("node at which the cycle was detected is:",c.info)

        p=c
        q=c
        len_cycle=0
        while True:
            len_cycle+=1
            q=q.link
            if p==q:
                break 
        print("length of cycle is :", len_cycle)

        len_rem_list=0
        p=self.start
        while p!=q:
            len_rem_list+=1
            p=p.link
            q=q.link
        print("number of not includee is cycle are :",len_rem_list)
        length_list=len_cycle+len_rem_list
        print("length of list is:",length_list)
        p=self.start
        for i in range(length_list-1):
            p=p.link
        p.link=None





list=SinglyLinkedList()
list.create_list()
list.display_list()

