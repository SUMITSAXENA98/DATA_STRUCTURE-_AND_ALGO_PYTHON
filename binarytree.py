class Node:
    def __init__(self,value):
        self.info=value
        self.lchild=None
        self.rchild=None

class BinaryTree:

    def __init__(self):
        self.root=None

    def is_empty(self):
        return self.root ==None


    def display(self):
        self.display(self.root,0)
        print()

    def display(self,p,level):
        if p is None:
            return 
        self._display(p.rchild,level+1)
        print()

        for i in range(level):
            print(" ", end='')
        print(p.info)
        self._display(p.lchild,level+1)



    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self,p):
        if p is None:
            return 
        print(p.info," ",end=" ")
        self._preorder(p.lchild)
        self._preorder(p.rchild)

    def inorder(self):
        self._inorder(self.root)
        return

    def _inorder(self):
        if p is None:
            return
        self._inorder(p.lchild)
        print(p.info," ",end=" ")
        self._inorder(p.rchild)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self,p):
        if p is None:
            return 
        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print(p.info," ",end="")

    def level_order(self):
        if self.root is None:
            print("tree is empty ")
            return 

        qu = deque()
        qu.append(self.root)

        while len(qu)!=0:
            p=qu.popleft()
            print(p.info+" ",end=" ")
            if p.lchild is not None:
                qu.append(p.lchild)
            if p.rchild id not None:
                qu.append(p.rchild)
    def height(self):
        return self._height(self.root)

    def _height(self,p):
        if p is None:
            return 0

        hl=self._height(p.lchild)
        hr=self._height(p.rchild)

        if hl>hr:
            return 1+hl
        else:
            return 1+hr

    def create_tree(self):
        self.root=Node('p')
        self.root.lchild=node('q')
        self.root.rchild=node('r')
        self.root.lchild.lchild=node('a')
        self.root.lchild.rchild=Node('b')
        self.root.rchild.lchild=node('x')

        



    




    
