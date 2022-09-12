class node:
     def __init__(self,data):
         self.data=data
         self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_node

    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


llist=LinkedList()
for i in range (5):
    
     llist.push(i)

llist.printlist()          

