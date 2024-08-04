
from queue import Queue
# Initializing a queue
my_queue = Queue(maxsize = 4)
# printing the present size of the queue
print(my_queue.qsize()) 
# Adding the data element to queue
my_queue.put('Apple')
my_queue.put('Mango')
my_queue.put('Banana')
my_queue.put('Orange')
# Return Boolean for Full Queue 
print("\nThe Queue is Full: ", my_queue.full()) 
# Removing the data element from queue
print("\nData Elements dequeued from the queue:")
print(my_queue.get())
print(my_queue.get())
print(my_queue.get())
print(my_queue.get())
# Return Boolean for Empty Queue
print("\nThe Queue is Empty: ", my_queue.empty())
my_queue.put("Kiwi")
print("\nThe Queue is Empty: ", my_queue.empty()) 
print("The Queue is Full: ", my_queue.full()) 