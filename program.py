# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def find_min_time(T, test_cases):
    results = []
    for i in range(T):
        N, K = test_cases[i][0]
        A = test_cases[i][1]
        B = test_cases[i][2]
        
        category_time = {}
        
        for j in range(N):
            category = A[j]
            time = B[j]
            if category in category_time:
                category_time[category] = min(category_time[category], time)
            else:
                category_time[category] = time
                
        if len(category_time) < K:
            results.append(-1)
            continue
        
        min_times = sorted (category_time.values())
        min_time = sum(min_times[:K])
        results.append(min_time)
        
    return results
    
input_data = """4
3 1
1 2 3
2 1 3
8 3
1 3 2 2 4 1 3 5
3 3 0 1 2 4 1 4
1 1
5
1
5 3
1 1 2 2 1
1 1 0 3 5
"""

import sys
from io import StringIO

sys.stdin = StringIO(input_data)


T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    test_cases.append(((N, K),A,B))
    
results = find_min_time(T, test_cases)
for result in results:
    print(result)
    
    
    