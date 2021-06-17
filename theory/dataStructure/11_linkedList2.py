'''
    링크드 리스트의 장단점
        장점
            미리 데이터 공간을 할당하지 않아도 됨 (배열은 미리 할당해야함)
        단점
            연결을 위한 별도의 공간 필요
            연결 정보를 찾는 시간이 필요하므로 접근 속도가 느림
            중간 데이터 삭제시, 앞뒤 데이터의 연결을 재구성해야 하는 부가적인 작업 필요


            
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while(node.next):
        node = node.next
    node.next = Node(data)

node1 = Node(1)
head = node1

for index in range(2,10):
    add(index)

node = head
while node.next:
#    print(node.data)
    node = node.next
#print(node.data)

#삽입
# 1. 앞 노드 찾기
node3 = Node(1.5)
node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

# 2. 포인터 교체 (들어갈 상위노드의 포인터가 들어갈 노드의 data를 가르켜야하고, 들어갈 노드의 poiner값에는 상위노드의 pointer가 들어가야함, 즉 상위노드의 next =  하위노드, 하위노드의 next = 상위노드의 next)
node_next = node.next #  <__main__.Node object at 0x0000022A15408F70>
node.next = node3
node3.next = node_next

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data) # 마지막꺼 출력 위해서!

'''
# 객체지향 프로그래밍으로 구현하기 
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '': # if there is no head
            self.head = Node(data)
        else:
            node = self.head
            while node.next:    # 참 수행 거짓 나감 
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

linkedlist1 = NodeMgmt(0)
#linkedlist1.desc()

for data in range(1, 10): # 1~9
    linkedlist1.add(data)

linkedlist1.desc()




        
        

