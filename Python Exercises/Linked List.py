
class Node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head= Node()

    def IsEmpty(self):
        if(self.head==None): print(" True ")
        else: print(" False ")

    def ToString(self):
        constring=' '
        nodeval = self.head
        while nodeval is not None:
            constring += str(nodeval.data)
            constring += ' '  
            nodeval = nodeval.next
        print(constring)

    def Find(self, data):
        currentnode= self.head
        while(currentnode!=None and currentnode.next!=data):
            currentnode= currentnode.next
        return currentnode.data


    def Add(self, data):
        new_node=Node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def Delete(self,index):
        if index>=self.length() or index<0:
            print ("ERROR: -999")
            return 
        cur_idx=0
        cur_node=self.head
        while True:
            last_node=cur_node
            cur_node=cur_node.next
            if cur_idx==index:
                last_node.next=cur_node.next
                return
            cur_idx+=1
            
datalist=SinglyLinkedList()
datalist.Add(1)
datalist.Add(2)
datalist.ToString()

# class DoublyLinkedList:
#     def __init__(self):
#         self.head=self.tail=Node()
    