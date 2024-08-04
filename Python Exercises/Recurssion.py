class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class linked_list:
	def __init__(self):
		self.head=node()

	# Adds new node containing 'data' to the end of the linked list.
	def append(self,data):
		new_node=node(data)
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_node

	# Returns the length (integer) of the linked list.
	def length(self):
		cur=self.head
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total 

	# Prints out the linked list in traditional Python list format. 
	def display(self):
            cur_node= self.head
            constring=''
            while cur_node.next !=None:
                cur_node= cur_node.next
                constring += str(cur_node.data)
                constring += " "
            print(constring)

	# Returns the value of the node at 'index'. 
	def Find(self,index):
		if index>=self.length() or index<0: # added 'index<0' post-video
			print ("ERROR: 'Get' Index out of range!")
			return None
		cur_idx=0
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_idx==index: return cur_node.data
			cur_idx+=1

	# Deletes the node at index 'index'.
	def Delete(self,data):
            HeadVal = self.head
            if (HeadVal is not None):
                if (HeadVal.data == data):
                    self.head = HeadVal.next
                    HeadVal = None
            while (HeadVal is not None):
                if HeadVal.data == data:
                    break
            prev = HeadVal
            HeadVal = HeadVal.next

            if (HeadVal == None):
                return

            prev.next = HeadVal.next
            HeadVal = None


	# Allows for bracket operator syntax (i.e. a[0] to return first item).
	def __getitem__(self,index):
		return self.get(index)

datalist=linked_list()
datalist.append(1)
datalist.append(2)
datalist.append(3)
datalist.Delete(2)
datalist.display()
