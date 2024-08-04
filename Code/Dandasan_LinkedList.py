class Node:
	def __init__(self, data=None):
            self.data=data
            self.tail=None

class NodeDoubly:
    def __init__(self, data):
        self.data = data
        self.nhead = None
        self.tail = None

class SinglyLinkedList:
    def __init__(self):
        self.head= Node()

    def new(self):
        self.head=None
    
    def IsEmpty(self):
        if(self.head==None): 
            print("True")
            return 1
        else: False

    def ToString(self):
            constring=' '
            printval = self.head
            while printval is not None:
                constring += str(printval.data)
                constring += " "
                printval = printval.tail
            print("[OUTPUT] --->",constring)

    def Find(self, finddata):
        findval= self.head
        nodenum=1   #Assumption for the number of node
        while findval != None and findval.data != finddata:
            findval= findval.tail
            nodenum +=1
        print("--- Value", finddata, "is in node", nodenum,"or at memory address of", findval," ---")

    def Add(self, data):
        NewNode = Node(data)
        node = self.head
        if self.head is None:
            self.head = NewNode
            return
        while(node.tail):
            node = node.tail
        node.tail=NewNode


    def Delete(self, deldata):
        if (self.IsEmpty()): print(" Error -999 ")
        delhead = self.head
        if (delhead  is not None):
            if (delhead .data == deldata):
                    self.head = delhead .tail
                    delhead  = None
                    return
            while (delhead  is not None):
                if delhead .data == deldata:
                    break
                prev = delhead 
                delhead  = delhead .tail

            if (delhead  == None):
                return
            prev.tail = delhead .tail
            delhead  = None


class DoublyLinkedList:
    def __init__(self):
        self.head= None

    def new(self):
        self.head=None

    def IsEmpty(self):
        if(self.head==None): 
            print("True")
            return 1
        else: False

    def ToString(self, node):
            constring=' '
            while node is not None:
                constring += str(node.data)
                constring += " "
                last = node
                node= node.tail
            print(constring)

    def Find(self, finddata):
        findval= NodeDoubly(finddata)
        nodenum=1   #Assumption for the number of node
        while findval != None and findval.data != finddata:
            findval= findval.tail
            nodenum +=1
        print("--- Value", finddata, "is in node", nodenum,"or at memory address of", findval," ---")

    def Add(self, data):
        choice= int(input(' Press 1: Add to Head\n Press 2: Add to Tail \n --> '))
        node = NodeDoubly(data)
        if choice==1:
            node.tail = self.head
            if self.head is not None:
                self.head.nhead = node
            self.head = node     
        elif choice ==2:
            node.tail = None
            if self.head is None:
                node.nhead = None
                self.head = node
                return
            last = self.head
            while (last.tail is not None):
                last = last.tail
            last.tail = node
            node.head = last
            return
    
    def Delete(self, deldata):
        choice= int(input(' Press 1: Delete from Head\n Press 2: Delete from Tail \n --> '))
        if (self.IsEmpty()): print(" Error -999 ")
        delhead = self.head

        if (delhead  is not None):
            if (delhead.data == deldata):
                    self.head = delhead .tail
                    delhead  = None
                    return
            while (delhead  is not None):
                if delhead .data == deldata:
                    break
                prev = delhead 
                delhead  = delhead .tail

            if (delhead  == None):
                return print(" Error -999 ")
            prev.tail = delhead .tail
            delhead  = None


class CircularLinkedList:

    def __init__(self):
        self.head=Node()
    
    def new(self):
        self.head=None

    def IsEmpty(self):
        if(self.head==None): 
            print("True")
            return 1
        else: False

    def ToString(self):
        constring=' '
        printval = self.head
        if self.head is not None:
            while(True):
                constring += str(printval.data)
                constring += " "
                printval = printval.tail
                if (printval == self.head):
                    break
            print("[OUTPUT] --->",constring[::-1])

    def Find(self, finddata):
        findval= self.head
        nodenum=1   #Assumption for the number of node
        while findval != None and findval.data != finddata:
            findval= findval.tail
            nodenum +=1
        print("--- Value", finddata, "is in node", nodenum,"or at memory address of", findval," ---")

    def Add(self, data):
      node = Node(data)
      nodetemp = self.head    
      node.tail = self.head
      if self.head is not None:
         while(nodetemp.tail != self.head):
            nodetemp = nodetemp.tail
         nodetemp.tail = node
      else:
         node.tail = node
      self.head = node

    def Delete(self, deldata):
        if (self.IsEmpty()): print(" Error -999 ")
        delhead = self.head
        if (delhead  is not None):
            if (delhead .data == deldata):
                    self.head = delhead .tail
                    delhead  = None
                    return
            while (delhead  is not None):
                if delhead .data == deldata:
                    break
                prev = delhead 
                delhead  = delhead .tail

            if (delhead  == None):
                return
            prev.tail = delhead .tail
            delhead  = None

def UserChoiceS2():
    usrchoice1= int(input("\n///////////////////////////////////////////////////// \
        \n\n*** Please Select from the Choices *** \n \
        \n Press 1: Singly Linked List\n Press 2: Doubly Linked List\
        \n Press 3: Cirular Linked List\n Press 4: EXIT\n  --> "))
    while True:
        if usrchoice1 == 4: break
        else: UserChoice(usrchoice1)


def UserChoice(usrchoice1):

    print(" (Please Create First a New List if you start unless the other choices will not function well)")
    first= True
    typelist=0
    if usrchoice1 == 1:
        datalist= SinglyLinkedList()
        print("\n\n\t\t*** Singly Link List ***")
        typelist==0
    elif usrchoice1 == 2:
        datalist= DoublyLinkedList()
        typelist +=1
        print("\n\n\t\t*** Doubly Link List ***")
        
    elif usrchoice1 == 3:
        datalist = CircularLinkedList()
        print("\n\n\t\t*** Circular Link List ***")
        typelist==0

    while(True):
        usrchoice2= int(input("\nPress 1: New List\nPress 2: IsEmpty List?\
                            \nPress 3: toString List\nPress 4: Find Node using Data\
                            \nPress 5: Add Data to List\nPress 6: Delete Data from List\nPress 7: EXIT\n --> "))
        if usrchoice2==1:
            datalist.new()
            first=False
        elif usrchoice2==2 and first==False:
            datalist.IsEmpty()
        elif usrchoice2==3 and first==False:
            if datalist.IsEmpty()==True:
                print("---  List is Empty yet!  ---")
            elif typelist is 1: datalist.ToString(datalist.head)
            else: 
                print(typelist)
                datalist.ToString()
        elif usrchoice2==4 and first==False:
            datalist.Find(input("Enter Data to Find: "))

        elif usrchoice2==5 and first==False:
            datalist.Add(input("Enter Data to Add: "))

        elif usrchoice2==6 and first==False:
            datalist.Delete(input("Enter Data to Delete: "))
        elif usrchoice2 == 7:
            UserChoiceS2()
        else: input(" No Yet List Created Please Create First! [ENTER]")

UserChoiceS2()







