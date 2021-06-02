'''
    이진 탐색 트리 삭제 
        매우 복잡함, 경우를 나누어서 이해하는 것이 좋음

        1. Leaf Node 삭제
            Leaf Node : Child Node가 없는 Node
            삭제할 Node의 Parent Node가 삭제할 Node를 가리키지 않도록 한다.
        2. Child Node가 하나인 Node 삭제
            삭제할 Node의 Parent Node가 삭제할 때 Node의 Child Node를 가리키도록 한다.
        3. Child Node가 두개인 Node 삭제
            삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키도록 한다.
            삭제할 Node의 왼쪽 자식 중, 가장 큰 값을 삭제할 Node의 Parent Node가 가리키도록 한다.

            
             
    
'''