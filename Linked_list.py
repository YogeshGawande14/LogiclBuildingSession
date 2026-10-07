class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_first(self):
        if self.head is None:
            return
        self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverse_recursive(self, node):
        if node is None or node.next is None:
            return node
        rest = self.reverse_recursive(node.next)
        node.next.next = node
        node.next = None
        return rest

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def merge_sorted(self, other):
        dummy = Node(0)
        tail = dummy
        a = self.head
        b = other.head
        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        if a:
            tail.next = a
        if b:
            tail.next = b
        merged = LinkedList()
        merged.head = dummy.next
        return merged

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Immediate calls to test functionality
ll = LinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
print("Initial list:")
ll.traverse()

ll.insert_begin(5)
print("After inserting at beginning:")
ll.traverse()

ll.delete_first()
print("After deleting first node:")
ll.traverse()

ll.delete_last()
print("After deleting last node:")
ll.traverse()

print("Search 20:", ll.search(20))
print("Search 99:", ll.search(99))

print("Count nodes:", ll.count_nodes())

ll.reverse_iterative()
print("After iterative reverse:")
ll.traverse()

ll.head = ll.reverse_recursive(ll.head)
print("After recursive reverse:")
ll.traverse()


list1 = LinkedList()
list1.insert_end(1)
list1.insert_end(3)
list1.insert_end(5)

list2 = LinkedList()
list2.insert_end(2)
list2.insert_end(4)
list2.insert_end(6)

merged = list1.merge_sorted(list2)
print("Merged sorted lists:")
merged.traverse()
