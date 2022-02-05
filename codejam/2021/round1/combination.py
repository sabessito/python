def combination(iter, r):
    t = tuple(iter)
    n = len(t)
    if r > n:
        return
    ind = list(range(r))
    yield tuple(t[i] for i in ind)
    while True:
        for i in reversed(range(len(ind))):
            if ind[i] != n - r + i:
                break
        else:
            return
        ind[i] += 1
        for j in range(i,r-1):
            ind[j+1] = ind[j] + 1
        yield tuple(t[i] for i in ind)

op = []
for i in combination('ABCDEF',2):
    op.append(''.join(i))
op