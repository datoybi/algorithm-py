'''
    노드와 포인터로 구성 
    node : 데이터의 저장 단위(데이터 값 ,포인터)
    pointer : 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

    __init__ : 초기화, 자바의 생성자같은 역할, 한 객체에 대한 인스턴스를 생성할 때 호출되는 것
    self : 인스턴스 자기 자신

# Node 구현
class Node:
    def __int__(self, data):
        self.data = data
        self.next = None

class Node:
    def __init__(self, data, next=None): # none이 있으면 값 넣어주고 없으면 none
        self.data = data
        self.next = next

node1 = Node(1) # make node
node2 = Node(2) # make node
node1.next = node2  # connect nodes
head = node1

'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
def add(data) :
    node = head
    while node.next: # 거짓이 될때 까지 수행
        node = node.next
    node.next = Node(data)

node1 = Node(1) # data : 1, next : none
head = node1

for index in range(2, 10): #1~9
    add(index)

# 출력
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)
