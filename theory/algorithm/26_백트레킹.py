"""
백 트래킹(backtracking) 또는 퇴각 검색(backtrack)으로 부름
    제약 조건 만족 문제에서 해를 찾기 위한 전략
        해를 찾기위해, 후보군에 제약 조건을 점진적으로 체크하다가, 해당 후보군이 제약 조건을 만족할 수 없다고 판단되는 즉시 backtrack(다시는 이 후보군을 체크하지 않을 것을 표기)하고,
        바로 다음 후보군으로 넘어가며, 결국 최적의 해를 찾는 방법
    실제 구현시, 고려할 수 있는 모든 경우의 수(후보군)를 상태공간트리(State Space Tree)를 통해 표현
        각 후보군을 DFS 방식으로 확인

    Promising: 해당 루트가 조건에 맞는지를 검사하는 기법 
    Pruning(가지치기) : 조건에 맞지 않으면 포기하고 다른 루트로 바로 돌아서서, 탐색의 시간을 절약하는 기법
"""

# N QUEEN 문제
# 대표적인 백트래킹 문제
# NxN 크기의 체스판에 N개의 퀸을 서로 공격할 수 없도록 배치하는 문제
# 퀸 : 수직, 수평, 대각선 이동(공격)가능

def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True


def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:]) # 얇은 복사
        return
    
    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate, final_result)
            current_candidate.pop()


def solve_n_queens(N):
    final_result = []
    DFS(N,0,[],final_result)
    return final_result


solve_n_queens(4)

