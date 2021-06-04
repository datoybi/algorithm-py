'''
    이진 탐색 트리 삭제의 경우의 수 
        매우 복잡함, 경우를 나누어서 이해하는 것이 좋음

        1. Leaf Node를 삭제 할 때
            Leaf Node : Child Node가 없는 Node ( 맨 끝 노드 )
            삭제할 Node의 Parent Node가 삭제할 Node를 가리키지 않도록 한다.
        2. Child Node가 하나인 Node 를 삭제 할 때
            삭제할 Node의 Parent Node가 삭제할 때 Node의 Child Node를 가리키도록 한다.
        3. Child Node가 두개인 Node 를 삭제 할 때 (복잡) 
            삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키도록 한다.
            삭제할 Node의 왼쪽 자식 중, 가장 큰 값을 삭제할 Node의 Parent Node가 가리키도록 할 경우
                1. 삭제할 노드의 오른쪽 자식 선택
                2. 오른쪽 자식의 가장 왼쪽에 있는 Node를 선택
                3. 해당 Node를 삭제할 Node의 Parent Node의 왼쪽 Branch가 가리키게 함 
                4. 해당 Node의 왼쪽 Branch가 삭제할 Node의 왼쪽 Child Node를 가리키게 함
                5. 해당 Node의 오른쪽 Branch가 삭제할 Node의 오른쪽 Child Node 가리키게 함
                6. 만약 해당 Node가 오른쪽 Child Node를 가지고 있었을 경우에는, 해당 Node의 본래 Parent의 왼쪽 Branch가 해당 오른쪽 Child Node를 가리키게 함
Divide and Conquer! 
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, head):
        self.head = head
    
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value: # current_node가 더 크다면 
                if self.current_node.left != None: # if is there any child node,
                      self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else: # current_node가 더 작다면
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else: 
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        # 먼저 해당 노드 찾고
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched == True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if searched == False:
            return False

        # 삭제하기
        # case 1: self.current_node가 삭제할 Node, self.parent는 삭제할 Node의 Parent Node인 상태
        if self.current_node.left == None and self.current_node.right == None: # Child가 없을때
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node
        
        # case2 : Child Node가 하나인 Node 를 삭제 할 때
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left

        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value :
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # case3 : 
        # 3-1:삭제할 Node가 Child Node를 두개 가지고 있을 경우 (삭제할 Node가 Parent Node 오른쪽에 있을 떄, 왼쪽에 있을 떄)
        # 3-1-1: 삭제할 노드의 parent node가 왼쪽에 있고 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 Child Node가 없을 때

        if self.current_node.left != None and self.current_node.right != None: # case 3
            if value < self.parent.value: # case 3-1
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self_change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left - self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.change_node.left
        else:         # 3-1-2: 삭제할 노드의 parent node가 왼쪽에 있고, 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 오른쪽에 Child Node가 있을 때
            self.change_node = self.current_node.right
            self.chenge_node_parent = self.current_node.right
            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None
            self.parent.right = self.change_node
            self.change_node.left = self.current_node.left
            self.change_node.right = self.current_node.right
        return True

'''
    random 라이브러리 활용
        random.randint(첫번째 숫자, 마지막 숫자): 첫번째 숫자부터 마지막 숫자 사이에 있는 숫자를 랜덤하게 선택해서 리턴
            예: random.randint(0, 99) : 0~99 사이의 숫자중 특정 수를 랜덤하게 선택하여 리턴

# 0 ~ 999 숫자 중에서 임의로 100개를 추출해서, 이진 탐색 트리에 입력, 검색, 삭제

'''
import random

# 0 ~ 999 중, 100개의 숫자 랜덤 선택
bst_nums = set() # 집합은 중복된 데이터를 가지고 있지 않음
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))
#print(bst_nums)

# 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)

# 입력한 100개의 숫자 검색 (검색 기능 확인)
    for num in bst_nums:
        if binary_tree.search(num) == False:
            print('search failed', num)

# 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
    delete_nums = set()
    bst_nums = list(bst_nums)
    while len(delete_nums) != 10:
        delete_nums.add(bst_nums[random.randint(0,99)])

# 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delete failed', del_num)

'''
# 팁
종이와 지우개로 rough한 코드를 작성해보고 그림을 그리고 케이스를 테스트해보자 
시간이 오래걸리지만 이해하기 용이
삭제 파트는 지금 말고 나중에 수업을 다 듣고 난 뒤에 작성해보는 것을 추천
그리고 마지막이 코드

# 이진 탐색 트리의 시간 복잡도와 단점
    시간 복잡도 (탐색시)
        depth (트리의 높이)를 h라고 표기한다면, O(h)
        n개의 노드를 가진다면, H = log2n에 가까우므로, 시간복잡도는 O(logn)
            참고 : 빅오 표기법에서 logn에서의 log밑은 10이 아니라 2이다.
                한번 실행시마다, 50%의 실행할 수도 있는 명령을 제거한다는 의미, 즉 50%의 시간을 단축시킬 수 있다는 것을 의미함

    단점
        최악의 경우는 링크드 리스트와 동일한 성능을 보여줌 (O(n))


'''