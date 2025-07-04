class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    

class LinkedList:

    def __init__(self):
        self.head=Node(None) 
        self.tail=None  
    
    def insert(self,data):
        new_node=Node(data)

        if self.head.next==None :
            self.head.next=new_node
            self.tail=new_node
        
        else:
            self.tail.next=new_node
            self.tail=new_node
    
    def delete(self,node):
        prev_node: Node =self.head
        curr_node : Node =self.head.next

        while curr_node!=None:
            if curr_node==node:
               prev_node.next=curr_node.next
               break
            prev_node=curr_node
            curr_node=curr_node.next

    def display(self):
        curr_node: Node = self.head.next
        while curr_node != None:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next
        print()

    def search(self, data) -> bool:
        curr_node: Node = self.head.next
        while curr_node != None:
            if curr_node.data == data:
                return True
            curr_node = curr_node.next
        return False


ll=LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)        
ll.insert(4)
ll.insert(5)
ll.display()
ll.delete(ll.head.next)
ll.delete(ll.head.next)
print(ll.search(3))
ll.display()