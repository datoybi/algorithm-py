
# 노드 클래스 만들기
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 이진 탐색 트리에 데이터 넣기 (작은값 왼쪽, 큰값 오른쪽)
class NodeMgmt:
    def __init__(self, head):
        self.head = head # root node
    
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value: # current_node.value 가 더 크면 -> 왼쪽
                if self.current_node.left == None:
                    self.current_node.left = Node(value)
                    break
                else:
                 self.current_node = self.current_node.left

            elif value >= self.current_node.value: # current_node.value가 더 작으면 -> 오른쪽
                if self.current_node.right == None:
                    self.current_node.right = Node(value)
                    break
                else:
                    self.current_node = self.current_node.right
    
    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            elif value >= self.current_node.value:
                self.current_node = self.current_node.right
        return False




head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)

print(BST.search(8))
print(BST.search(1000))

