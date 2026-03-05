class Node:
    def __init__(self,value):
        self.val=value
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0
        

    def get(self, index: int) -> int:
        if index>=self.size or index<0:
            return -1
        
        curr=self.head
        for _ in range(index):
            curr=curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        a=Node(val)
        a.next=self.head
        self.head=a
        self.size+=1

    def addAtTail(self, val: int) -> None:
        a=Node(val)

        if not self.head:
            self.head=a
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=a

        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        a=Node(val)

        if index>self.size:
            return

        if index==0:
            self.addAtHead(val)
            return 

        else:
            curr=self.head
            for _ in range(index-1):
                curr=curr.next
            a.next=curr.next
            curr.next=a
        self.size+=1
        

    def deleteAtIndex(self, index: int) -> None:
        curr=self.head
        if index<0 or index>=self.size:
            return 
        elif index==0:
            self.head=self.head.next
            
        else:
            for _ in range(index-1):
                curr=curr.next
            curr.next=curr.next.next

        self.size-=1
    
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)