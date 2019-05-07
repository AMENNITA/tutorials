class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node  # Only for Double Linked List

    def __repr__(self):
        return repr(self.data)


# Class to Implement Linked List
class LinkedList:
    # Constructor method
    def __init__(self):
        self.head = None
        self.size = 0

    # Print method for Class
    def __repr__(self):
        nodes = []
        tmp = self.head
        while tmp:
            nodes.append(repr(tmp))
            tmp = tmp.next_node
        return "[" + ", ".join(nodes) + "]\n"

    # Inset method
    def insert(self, data=None):
        # Assign a value to Head Node if Null
        if self.head is None:
            self.head = Node(data)
            self.size = 1
        else:
            tmp = self.head
            while tmp.next_node is not None:
                tmp = tmp.next_node
            tmp.next_node = Node(data)
            self.size += 1

    # Get the size
    def get_size(self):
        return self.size

    # Remove an element
    def remove(self, key):
        if key is None or not key.isdigit():
            print("Invalid Key : {}, Should be an Integer between 1 and {}".format(key, self.size))
        elif int(key) > self.size:
            print("Key should be between 1 and {}".format(self.size))
        elif int(key) == 1:
            self.head = self.head.next_node
            self.size -= 1
        else:
            tmp, pos = self.head, 0
            while tmp and pos + 1 < int(key):
                pos += 1
                tmp = tmp.next_node
            tmp.next_node = (tmp.next_node).next_node
            self.size -= 1

    # Get element at the given key
    def get(self, key):
        try:
            if int(key) > self.size:
                print("Invalid Key : {}, Should be an Integer between 1 and {}".format(key, self.size))
            else:
                tmp, pos = self.head, 1
                while tmp and pos < int(key):
                    pos, tmp = pos + 1, tmp.next_node
                # Return Data
                return tmp.data
        except:
            print("Invalid Key : {}, Should be an Integer value between 1 and {}".format(key, self.size))

# Class to Implement Double LinkedList
class DoubleLinkedList:
    # Constructor method
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.head = None
        self.size = 0

    # Repr method
    def __repr__(self):
        nodes = []
        tmp = self.head
        while tmp:
            nodes.append(repr(tmp))
            tmp = tmp.next_node
        return "[ {} ]".format(", ".join(nodes))

    def insert(self, data=None):
        if self.head is None:
            self.head, self.size = Node(data), 1
        else:
            tmp = self.head
            while tmp.next_node is not None:
                tmp = tmp.next_node
            # Assign the value
            tmp.next_node = Node(data, None, tmp)
            # tmp.next_node.prev_node = tmp
            self.size += 1

    def remove(self, key):
        try:
            if int(key) > self.size:
                print("Invalid Key : {}, Should be an Integer between 1 and {}".format(key, self.size))
            elif int(key) == 1:
                self.head = self.head.next_node
                self.head.prev_node = None
                self.size -= 1
            else:
                tmp, pos = self.head, 1
                while pos + 1 < key:
                    pos, tmp = pos + 1, tmp.next_node
                tmp.next_node = (tmp.next_node).next_node
                tmp.next_node.prev_node = tmp
                self.size -= 1
        except:
            print("Invalid Key : {}, Should be an Integer value between 1 and {}".format(key, self.size))

    def get(self, key):
        try:
            if int(key) > self.size:
                print("Invalid Key : {}, Should be an Integer between 1 and {}".format(key, self.size))
            else:
                tmp, pos = self.head, 1
                while pos < key:
                    pos, tmp = pos + 1, tmp.next_node
                return "{{} : {}".format(key, tmp.data)
        except:
            print("Invalid Key : {}, Should be an Integer value between 1 and {}".format(key, self.size))
