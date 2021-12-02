N = int(input())
S = input()
dic = {
    'A': {'A': 'A', 'G': 'C', 'C': 'A', 'T': 'G'},
    'G': {'A': 'C', 'G': 'G', 'C': 'T', 'T': 'A'},
    'C': {'A': 'A', 'G': 'T', 'C': 'C', 'T': 'G'},
    'T': {'A': 'G', 'G': 'A', 'C': 'G', 'T': 'T'}
}
for _ in range(N - 1):
    new = dic[S[-1]][S[-2]]
    S = S[:-2] + new
print(S)