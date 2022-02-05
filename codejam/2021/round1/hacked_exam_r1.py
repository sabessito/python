from fractions import Fraction

T = int(input())
for t in range(T):
    N, Q = list(map(int,input().split()))
    ans_dict = {i : [] for i in range(Q)}
    exp_score_dict = {i : [] for i in range(Q)}
    for _ in range(N):
        ans, score = list(input().split())
        ans = list(ans)
        score = int(score)
        if score/Q < 1/2:
            score = Q - score
            for i in range(len(ans)):
                if ans[i] == 'T':
                    ans_dict[i].append('F')
                    exp_score_dict[i].append(Fraction(score,Q))
                else:
                    ans_dict[i].append('T')
                    exp_score_dict[i].append(Fraction(score,Q))
        else:
            for i in range(len(ans)):
                if ans[i] == 'T':
                    ans_dict[i].append('T')
                    exp_score_dict[i].append(Fraction(score,Q))
                else:
                    ans_dict[i].append('F')
                    exp_score_dict[i].append(Fraction(score,Q))
    final_ans = ''.join([ans_dict[i][exp_score_dict[i].index(max(exp_score_dict[i]))] for i in range(Q)])
    final_ans_score = sum([max(exp_score_dict[i]) for i in range(Q)])
    print(f'Case #{t+1}: {final_ans} {final_ans_score.numerator}/{final_ans_score.denominator}')