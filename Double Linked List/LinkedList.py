import random
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def find(self, new_data):
        count = 0
        current = self.head
        while current != None:
            count += 1
            if current.data == new_data:
                print("Position in List: ", count)
                return True
            current = current.next
        print("Not in List")
        return False

    def length(self):
        count = 0
        temp = self.head
        while temp != None:
            count += 1
            temp = temp.next
        print("Length: ", count)
        return count

    def addNode(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def returnAll(self):
        output = []
        if self.head:
            temp = self.head
            while temp:
                output.append(temp.data)
                temp = temp.next
            print(output)

    def addAfterNode(self, pos, new_data):
        if pos is None:
            print('Linked List is empty')
            return
        position = self.head
        try:
            while position is not None:
                if position.data == pos:
                    break
                position = position.next
            new_node = Node(new_data)
            new_node.next = position.next
            position.next = new_node
        except AttributeError:
            return

    def addBeforeNode(self, pos, node_data):
        if pos is None:
            print("Linked List is empty")
            return
        position = self.head
        new_node = Node(node_data)
        try:
            while position is not None:
                if position.next.data == pos:
                    break
                position = position.next
            new_node.next = position.next
            position.next = new_node
        except AttributeError:
            return

    def removeBeforeIndex(self, node_after_delete):
        if node_after_delete.prev is None:
            return
        if node_after_delete.prev.prev is not None:
            node_after_delete.prev = node_after_delete.prev.prev
            node_after_delete.prev.next = node_after_delete
        else:
            node_after_delete.prev = node_after_delete
            self.head = node_after_delete

    def removeAfterIndex(self, node_before_delete):
        if node_before_delete.next is None:
            return
        if node_before_delete.next.next is not None:
            node_before_delete.next = node_before_delete.next.next
            node_before_delete.next.prev = node_before_delete
        else:
            node_before_delete.next = None
            self.tail = node_before_delete

    def sortListASC(self):
        if(self.head == None):
            return
        else:
            current = self.head
            while(current.next != None):
                index = current.next
                while(index != None):
                    if(current.data > index.data):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next

    def sortListDESC(self):
        if (self.head == None):
            return
        else:
            current = self.head
            while (current.next != None):
                index = current.next
                while (index != None):
                    if (current.data < index.data):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next#

    def sum(self):
        sum = 0
        temp = self.head
        while temp is not None:
            sum += temp.data
            temp = temp.next
        print(sum)
        return sum

    def avg(self):
        if(self.head == None):
            return
        else:
            sum = self.sum()
            len = self.length()
            return print("AVG: ", sum/len)

    def max(self):
        if(self.head == None):
            return
        else:
            temp = self.head
            temp2 = temp.data
            while temp != None:
                if temp.data > temp2:
                    temp2 = temp.data
                temp = temp.next
            return print("max: ", temp2)

    def min(self):
        if(self.head == None):
            return
        else:
            temp = self.head
            temp2 = temp.data
            while temp != None:
                if temp.data < temp2:
                    temp2 = temp.data
                temp = temp.next
            return print("min: ", temp2)


if __name__ == '__main__':
    llist = LinkedList()
    for i in range(20):
        llist.addNode(random.randint(0, 10))
    llist.returnAll()
    print("")
    llist.addAfterNode(9, 100)
    llist.addBeforeNode(9, 100)
    llist.returnAll()
    print("")
    llist.removeAfterIndex(llist.head)
    llist.returnAll()
    llist.removeBeforeIndex(llist.tail)
    llist.returnAll()
    print("")
    start = time.time()
    llist.sortListASC()
    end = time.time()
    print("Time to Sort", end-start)
    llist.returnAll()
    llist.sortListDESC()
    llist.returnAll()
    print("")
    llist.sum()
    llist.avg()
    llist.max()
    llist.min()
    llist.find(9)
    llist.length()
    print("")