'''
링크드 리스트의 노드 삭제
    head 삭제
    마지막 노드 삭제
    중간 노드 삭제


'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head =='':
            self.head = Node(data)
        else:          
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
    
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다.")
            return

        if self.head.data == data: #삭제할 노드가 head인 경우
            temp = self.head
            self.head = self.head.next
            del temp # temp를 만들지 않고 걍 삭제 가넝 한?
        else:   
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next
                
# delete head 
linkedList1 = NodeMgmt(0)
print(linkedList1.head)
linkedList1.delete(0)
print(linkedList1.head)

# delete middle node 
linkedList1 = NodeMgmt(0)
for data in range(1,10):
    linkedList1.add(data)
linkedList1.desc()
print("--")
linkedList1.delete(5)
linkedList1.desc()

# delete last node 
print("--")
linkedList1.delete(9)
linkedList1.desc()

