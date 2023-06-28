queue = []
def enqueue():
    if len(queue) == n:
        print("The queue is full")
    else:
        element = input("Enter an element:")
        queue.insert(0, element)
        print("Update queue is:", queue)
def dequeue():
    if len(queue)==0:
        print("Queue is empty")
    else:
        r=queue.pop(0)
        print("The deleted element is {}".format(r))
        print("Updted queue is",queue)
def isFull():
    if len(queue)==n:
        print("The queue is full")
def isEmpty():
    if len(queue)>=0 and len(queue)<n:
        print("The queue have some spaces to store")
    elif len(queue)==0:
        print("The queue is empty")

n=int(input("Enter the size of the queue:"))

while True:
    print("""Enter the choice given below to perform Queue operations
  
       1.Enqueue
       2.Dequeue
       3.IsFull
       4.IsEmpty
       5.Exit""")
    choice=int(input("Enter your choice:"))

    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        isFull()
    elif choice==4:
         isEmpty()
    elif choice==5:
        print("The process was terminated")
        break
    else:
        print("Enter the valid input man")
