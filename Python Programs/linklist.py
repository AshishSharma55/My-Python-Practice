print("Easy way")
class list:
    def __init__(self,data,nextnode=None):
        self.data=data
        self.nextnode=nextnode
node1=list("1")
node2=list("2")
node3=list("3")
node1.nextnode=node2
node2.nextnode=node3
head=node1
while True:
    print(head.data,"-->",end ="")
    if head.nextnode is None:
        print("None")
        break;
    head=head.nextnode
print()
print("Now another way")
class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class linklist:
    def __init__(self):
        self.head=None
        
    def insert(self,data):
        new=node(data)
        if self.head is None:
            self.head=new
            return
        currentnode=self.head
        while True:
            if currentnode.next is None:
                currentnode.next=new
                break;
            currentnode=currentnode.next
    def printlist(self):
        currentnode=self.head
        while currentnode is not None:
            print(currentnode.data,"-->",end='')
            currentnode=currentnode.next
        print("None")
ll=linklist()
ll.printlist()

ll.insert("1")
ll.insert("2")
ll.insert("3")
ll.printlist()



