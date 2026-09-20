import sys

def solve():
    # 첫 번째 줄: N과 S 입력
    n, s = map(int, sys.stdin.readline().split())
    
    # 두 번째 줄: N개의 숫자 입력
    arr = list(map(int, sys.stdin.readline().split()))
    
    # 모든 숫자의 전체 합 구하기
    total_sum = sum(arr)
    
    # 최솟값을 저장할 변수를 무한대(inf)로 초기화
    min_diff = float('inf')
    
    # 제외할 서로 다른 2개의 숫자 인덱스(i, j)를 고르는 완전 탐색
    for i in range(n):
        for j in range(i + 1, n):
            # 전체 합에서 두 숫자를 제외한 나머지 합 (T)
            t = total_sum - arr[i] - arr[j]
            
            # |T - S|의 절대값 차이 계산
            diff = abs(t - s)
            
            # 최솟값 갱신
            if diff < min_diff:
                min_diff = diff
                
    # 결과 출력
    print(min_diff)

if __name__ == '__main__':
    solve()