# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 08:44:46 2022

@author: student
"""

# # ====================Linear Queue Functions Algorithm  ========================================

queueData=[]   

#New Operation
def newQueue(size):
     queueData= [None]*size                     #queue size

def clearQueue():
     queueData.clear()
     return print("Clear Complete")             #clear data in queue
     
def isEmpty():
     if (queueData==[]):                        #return True if queue is empty
         return True
     else: return False
 
def isFull(index, size):
     if((index==size)): return True             #return True if the current index is mod to total size
     else: return False

def enqueue(data, index, size):
     if((index)== size):
        print("\n==== Overflow Error ====")
     else: 
        queueData.append(data)
        return True
     
def dequeue():
    if(isEmpty()): 
        print("\n==== Underflow Error ====")
    else: 
        queueData.pop(0)
        return True
     
def peek():
     return queueData[0]

index=0
while(True):                                    # Infinite While loop for choice, it breaks if none of the give character chosen or h
    print("\na.] Create new Queue    e.] Enqueue  \
           \nb.] Clear Queue         f.] Dequeue \
           \nc.] Is Empty Queue?     g.] Peek \
           \nd.] Is Full Queue?      h.] Exit \n")
                
    choice= str(input("Enter Choice: "))

    if(choice=='a'):
        size= int(input("Enter Queue size: "))
        newQueue(size)

    elif(choice=='b'):
        clearQueue()
        index=0

    elif(choice=='c'):
        print("--->",isEmpty())

    elif(choice=='d'):
        print("--->", isFull(index, size))

    elif(choice=='e'):
        if(enqueue(input("\nEnter Data: "),index, size)):
            index +=1
        print(queueData)

    elif(choice=='f'):
        if(dequeue()): index -=1
        print(queueData)

    elif(choice=='g'):
        print("--->",peek())

    else: break








# #======================= LINEAR QUEUE IMPLEMENTATION ==================#
# #New Implementation
# size= 5   #assume maxsize is 5
# queue=[1,2,3,4,5]  #5 data values

# #Clear Implementation
# queue.clear()

# #isEmpty Implementation
# if (queue==[]): print("True")
# else: print("False")

# #isFull
# if (len(queue)==size): print(True)
# else: print(False)

# #enqueue
# if(len(queue)==size):
#     print("Overflow Error")
# else:
#     queue.append()

# #dequeue
# if(queue[0]==False):        #list is empty
#     print("Underflow Error")
# else:
#     queue.pop(0)

# #peek
# print(queue[0])
    
    