


# ====================Linear Queue Functions Algorithm  ========================================
 #New Operation
queueData=[]
index=0
def newQueue(size):
     queueData= [None]*size         #queue size

def clearQueue():
     queueData.clear()
     return print("Clear Complete")            #clear data in queue
     
def isEmpty():
     if (queueData==[]):         #return True if queue is empty
         return True
     else: return False
 
def isFull(size):
     if((index==size)): return True   #return True if the current index is mod to total size
     else: return False

def enqueue(data, size):
     if((index)== size): print("\n==== Overflow Error ====")
     else: queueData.append(data)
     
def dequeue():
    if(isEmpty()): print("\n==== Underflow Error ====")
    else: return queueData.pop(0)
     
def peek():
     return queueData[0]

while(True):
    print("\na.] Create new Queue    e.] Enqueue  \
           \nb.] Clear Queue         f.] Dequeue \
           \nc.] Is Empty Queue?     g.] Peek \
           \nd.] Is Full Queue?      h.] Exit \n")
                    \
  
    choice= str(input("Enter Choice: "))

    if(choice=='a'):
        size= int(input("Enter Queue size: "))
        newQueue(size)

    elif(choice=='b'):
        clearQueue()

    elif(choice=='c'):
        print("--->",isEmpty())

    elif(choice=='d'):
        print("--->", isFull(size))

    elif(choice=='e'):
        enqueue(input("\nEnter Data: "),size)
        index+=1
        print(queueData)

    elif(choice=='f'):
        dequeue()
        print(queueData)

    elif(choice=='g'):
        print("--->",peek())

    else: break