class ListNode:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        dummy = ListNode('dummy')
        dummy.next = dummy.previous = dummy
        self.head = self.tail = dummy
    def append(self, node):
        node.next = self.tail
        node.previous = self.tail.previous
        self.tail.previous.next = node
        self.tail.previous = node
    def remove(self, node):
        node.previous.next = node.next
        node.next.previous = node.previous
    def popleft(self):
        node = self.head.next
        self.remove(node)
        return node
    def print(self):
        node = self.head.next
        while node != self.tail:
            print(node.value)
            node = node.next
from collections import namedtuple, defaultdict
Customer = namedtuple('Customer', ['name', 'party_size'])
class WaitList:
    def __init__(self, sizes):
        self.tables = defaultdict(int)
        for table in sizes:
            self.tables[table] += 1
        # table size => doubly linked list
        self.waiting = defaultdict(DoublyLinkedList)
        # customer => node from the doubly linked list
        self.customers = dict()
    def add(self, customer):
        table = customer.party_size
        self.tables[table] -= 1
        node = ListNode(customer)
        self.waiting[table].append(node)
        self.customers[customer] = node
    def remove(self, customer):
        table = customer.party_size
        self.tables[table] += 1
        node = self.customers[customer]
        self.waiting[table].remove(node)
        del self.customers[customer]
    def serve(self, seats):
        table = seats
        node = self.waiting[table].popleft()
        customer = node.value
        self.remove(customer)
        print('served', customer.name)
sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wl = WaitList(sizes)
bob1 = Customer('Bob1', 4)
wl.add(bob1)
bob2 = Customer('Bob2', 4)
wl.add(bob2)
wl.serve(4) # served Bob1
wl.serve(4) # served Bob2
tom = Customer('Tom', 10)
wl.add(tom)
wl.remove(tom)
wl.add(tom)
wl.serve(10) # served Tom
