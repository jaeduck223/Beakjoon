import sys
input = sys.stdin.readline

def valid_states(row_mask, C):
    states = []
    for s in range(1 << C):
        if s & row_mask:                
            continue
        if s & (s << 1):                
            continue
        states.append(s)
    return states

def max_students(R, C, classroom):
    broken = []
    for r in range(R):
        mask = 0
        for c, ch in enumerate(classroom[r]):
            if ch == 'x':
                mask |= (1 << c)
        broken.append(mask)

    row_states = [valid_states(broken[r], C) for r in range(R)]

    from collections import defaultdict
    dp = {0: 0}

    for r in range(R):
        ndp = defaultdict(int)
        for cur in row_states[r]:
            cur_cnt = cur.bit_count()    
            for prev, val in dp.items():
                if (cur & (prev << 1)) or (cur & (prev >> 1)):
                    continue         
                ndp[cur] = max(ndp[cur], val + cur_cnt)
        dp = ndp                      

    return max(dp.values())

# ---- main ----
T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    classroom = [input().strip() for _ in range(R)]
    print(max_students(R, C, classroom))


