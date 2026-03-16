n, m = map(int, input().split())

set_result = float('inf')
each_result = float('inf')

for _ in range(m):
    a, b = map(int, input().split())

    set_result = min(set_result, a)
    each_result = min(each_result, b)

all_set_result = ((n // 6) + 1) * set_result  

mix_result = (n // 6) * set_result + (n % 6) * each_result  

all_each_result = n * each_result  

print(min(all_set_result, mix_result, all_each_result))