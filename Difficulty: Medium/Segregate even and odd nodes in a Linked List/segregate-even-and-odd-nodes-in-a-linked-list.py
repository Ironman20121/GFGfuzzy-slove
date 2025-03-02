# User function Template for Python3

# Following is the structure of node 
# class node:
#     def __init__(self):  
#         self.data = None
#         self.next = None

class Solution:
    def divide(self, head):
        # code here
        
        def isEven(node):return (node.data %2 ==0)
        
        # to avoid edge cases
        evenHead = node()
        oddHead = node()
        
        eventail = evenHead
        oddtail = oddHead
        
        curr = head
        
        while curr:
            
            if isEven(curr):
                eventail.next = curr
                eventail  = eventail.next
            else :
                oddtail.next = curr
                oddtail = oddtail.next
    
            curr = curr.next
        
        
        oddtail.next = None
        
        if evenHead.next:
            eventail.next = oddHead.next
            return evenHead.next
        
        return oddHead.next
    
    
    
        
       
       

#{ 
 # Driver Code Starts
# Initial Template for Python3


# Node Class
class node:

    def __init__(self):
        self.data = None
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next


def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()

        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob = Solution()
        newhead = ob.divide(list1.head)
        printlist(newhead)

        print("~")

# } Driver Code Ends