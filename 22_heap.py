'''
    힙과 배열 
        일반적으로 힙 구현시 배열 자료구조를 활용함
        배열은 인덱스가 0번부터 시작하지만, 힙 구현의 편의를 위해, root 노드 인덱스 번호를 1로 지정하면, 구현이 좀더 수월함
            부모 노드 인덱스 번호(parent node's index) = 자식 노드 인덱스 번호 (child node's index) //2
            왼쪽 자식 노드 인덱스 번호 (left child node's index) = 부모 노드 인덱스 번호 (parent node's index) *2
            오른쪽 자식 노드 인덱스 번호 (right child node's index) = 부모 노드 인덱스 번호 (parent node's index) *2+1

'''
# 힙의 데이터 삽입
#  1. 완전 이진트리처럼 데이터 채우기 2. 부모노드와 비교를 해서 부모노드보다 작을 떄 까지 바꿔주는 작업
class Heap:
    #완전 이진트리처럼 데이터 채우기
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        if inserted_idx <=1:
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        self.heap_array.append(data)
    #  부모노드와 비교를 해서 부모노드보다 작을 떄 까지 바꿔주는 작업  
        inserted_idx = len(self.heap_array)-1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx//2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx] # swap
            inserted_idx = parent_idx

        return True


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
