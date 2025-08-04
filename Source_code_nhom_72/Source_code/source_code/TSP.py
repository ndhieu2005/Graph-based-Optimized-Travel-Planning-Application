# TSP.py

def notIn(i, subset):
    return ((1 << i) & subset) == 0

def combinations(r, N):
    subsets = []
    combinationsRep(0, 0, r, N, subsets)
    return subsets

def combinationsRep(set_mask, at, r, N, subsets):
    if r == 0:
        subsets.append(set_mask)
    else:
        for i in range(at, N):
            set_mask |= (1 << i)
            combinationsRep(set_mask, i + 1, r - 1, N, subsets)
            set_mask &= ~(1 << i)

def setup(m, memo, S, N):
    # Khởi tạo base case: mọi i != S, subset = {S, i}, cost = m.get_value(S, i)
    for i in range(N):
        if i == S:
            continue
        state = (1 << S) | (1 << i)
        memo.insert(i, state, m.get_value(S, i))

def solve(m, memo, S, N):
    # Ta chỉ lặp r = 3..N (tức độ lớn của tập con)
    # r là số lượng đỉnh trong subset (kể cả S)
    for r in range(3, N + 1):
        for subset in combinations(r, N):
            if notIn(S, subset):
                continue
            # Với mỗi đỉnh 'nxt' nằm trong subset và nxt != S
            for nxt in range(N):
                if nxt == S or notIn(nxt, subset):
                    continue
                # state = subset nhưng chưa có 'nxt'
                state = subset ^ (1 << nxt)
                minDist = float('inf')
                # Tìm e sao cho e ∈ state, e != S
                for e in range(N):
                    if e == S:
                        continue
                    if notIn(e, state):
                        continue
                    dist_e_to_nxt = memo.get_value(e, state) + m.get_value(e, nxt)
                    if dist_e_to_nxt < minDist:
                        minDist = dist_e_to_nxt
                memo.insert(nxt, subset, minDist)

def findMinCost(m, memo, S, N):
    END_STATE = (1 << N) - 1
    minTourCost = float('inf')
    for e in range(N):
        if e == S:
            continue
        cost_full = memo.get_value(e, END_STATE) + m.get_value(e, S)
        if cost_full < minTourCost:
            minTourCost = cost_full
    return minTourCost

def findOptimalTour(m, memo, S, N):
    lastIndex = S
    state = (1 << N) - 1
    tour = [None] * (N + 1)

    # Lùi từ cuối full-set để tìm đỉnh trước
    for i in range(N - 1, 0, -1):
        idx = -1
        best = float('inf')
        for j in range(N):
            if j == S:
                continue
            if notIn(j, state):
                continue
            # Tính cost nếu trước 'lastIndex' từng là j
            c = memo.get_value(j, state) + m.get_value(j, lastIndex)
            if c < best:
                best = c
                idx = j
        tour[i] = idx
        state ^= (1 << idx)
        lastIndex = idx

    tour[0] = S
    tour[N] = S  # để hoàn thành vòng
    return tour

def tsp(m, S, locations):
    import Matrix
    import Graph

    N = m.size('row')
    # Tạo ma trận memo kích thước [N x 2^N]
    memo = Matrix.matrix(N, int((1 << N)))
    # Bình thường hóa tên vị trí
    locations_normalized = Graph.Dict()      # sửa Graph.dict() → Graph.Dict()
    for i in range(N):
        locations_normalized.insert(i, locations[i])

    # Tính DP
    setup(m, memo, S, N)
    solve(m, memo, S, N)

    # In ra ma trận memo (tùy nếu bạn muốn debug)
    # print(">> Ma trận memo (hàng = đỉnh kết thúc, cột = subset bitmask):")
    # for i in range(N):
    #     for j in range(1 << N):
    #         print(f"{memo.get_value(i, j):>5}", end=' ')
    #     print()

    minCost = findMinCost(m, memo, S, N)
    tour = findOptimalTour(m, memo, S, N)

    # Chuyển các chỉ số về nhãn vị trí ban đầu
    for i in range(len(tour)):
        tour[i] = locations_normalized.lookup(tour[i])

    return minCost, tour
