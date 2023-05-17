class Node:
    def __init__(self, data, next) -> None:
        self.data = data 
        self.next = next
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    # insert a node at the beginning of the linked list
    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node
    
    # insert a node at the end of the linked list
    def insert_at_end(self, data):
        node = Node(data, None)
        if (self.head == None):
            self.head = node
            
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node
    
    # insert a node at the specific position 
    def insert_at_n(self,data, pos):
        node = Node(data, self.head)
    
        count = 1
        itr = self.head

        while (count < pos):
            itr = itr.next
            count+= 1
        
        self.head = itr.next
        itr.next = node

     # function to print the visual representation of linked list    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        x =''
        while itr:
            x += str(itr.data) + '----------->'
            itr= itr.next
        print(x)


    # inserts values as list
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    # calculate the length of the linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+= 1
            itr= itr.next
        return count



    # remove the values at given index
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')
        
        if index==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1 
    


if __name__ == "__main__":
    ll = LinkedList()

    # ll.insert_at_start(10)
    # ll.insert_at_start (13)
    # the above code prints  13------>10----->

    # ll.insert_at_end(34)
    # ll.insert_at_end(56)
    # the above code prints  34----->56----->


    # ll.insert_values(["cat", "bat", "rat", "bear", "deer"])
    #the above code prints cat----------->bat----------->rat----------->bear----------->deer----------->

    # ll.get_length()
    # ll.remove_at(2)    #cat----------->bat----------->bear----------->deer-----------> ; here 'bat' which is at index 2 is removed


    ll.print()
