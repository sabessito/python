from fractions import Fraction

T = int(input())
for t in range(T):
    N, Q = list(map(int,input().split()))
    T_score = {q:0 for q in range(Q)}
    F_score = {q:0 for q in range(Q)}
    final_ans = []
    final_score = 0
    for _ in range(N):
        ans, score = list(input().split())
        ans = list(ans)
        score = int(score)
        for q in range(Q):
            if ans[q] == 'T':
                T_score[q] += score
                F_score[q] += Q - score
            else:
                T_score[q] += Q - score
                F_score[q] += score
    for q in range(Q):
        if T_score[q] >= F_score[q]:
            final_ans.append('T')
            final_score += Fraction(T_score[q],Q*N)
        else:
            final_ans.append('F')
            final_score += Fraction(F_score[q],Q*N)
    final_ans = ''.join(final_ans)
    print(f'Case #{t+1}: {final_ans} {final_score.numerator}/{final_score.denominator}')
