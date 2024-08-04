
class Node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head= Node()

    def new(self):
        self.head= None

    def IsEmpty(self):
        if(self.head==None): print(" True ")
        else: print(" False ")

    def ToString(self):
        listdata=[]
        thenode=self.head
        while(thenode.next!=None):
            thenode=thenode.next
            listdata.append(thenode.data)
        print(*listdata)

    def Find(self, data):
        currentnode= self.head
        while(currentnode!=None and currentnode.next!=data):
            currentnode= currentnode.next
        return currentnode.data


    def Add(self, data):
        new_node= Node(data)
        currentnode= self.head
        while currentnode.next!=None:
            currentnode=currentnode.next
        currentnode.next=new_node

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
            
datalist= SinglyLinkedList()
datalist.new()

datalist.IsEmpty()

# class DoublyLinkedList:
#     def __init__(self):
#         self.head=self.tail=Node()
    