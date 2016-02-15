class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
        self.ptr = head

    def insert(self, data):
        new_node = Node(data)
        if self.head==None:
            self.head=data
        new_node.set_next(self.ptr)
        self.ptr = new_node

    def size(self):
        current = self.ptr
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def headdisp(self):
        print self.head

    def search(self, data):
        current = self.ptr
        found = False
        pos=1
        while current and found is False:
            if current.get_data() == data:
                found = True
                print "%dth position of element data %d" %(pos,data)
            else:
                current = current.get_next()
                pos+=1
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.ptr
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
