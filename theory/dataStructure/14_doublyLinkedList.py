'''
doubly linked list 이중연결리스트
장점
    양 방향으로 연결되어 있어서 노드 탐색이 양쪽으로 모두 가능 

'''

class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
    
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new 

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_from_head(self,data):
        if self.head == None:
            return False

        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self,data):
        if self.head == None:
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    def insert_before(self, data, before_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new
            return True

    def insert_after(self, data, after_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if node == None:
                    return False
            new = Node(data)
            after_new = node.next  
            after_new.prev = new
            new.next = after_new
            new.prev = node
            node.next = new 
            if new.next == None:
                return True

doubly_linked_list = NodeMgmt(0)
for data in range(1,10):
    doubly_linked_list.insert(data)
'''
doubly_linked_list.desc()

node3 = doubly_linked_list.search_from_head(3)
print(node3.data,"\n")
        
        
node5 = doubly_linked_list.search_from_tail(5)
print(node5.data ,"\n")

doubly_linked_list.insert_before(1.5, 2)
doubly_linked_list.desc()

print("\n\n")
'''
doubly_linked_list.insert_after(1.5, 1)
doubly_linked_list.desc()

