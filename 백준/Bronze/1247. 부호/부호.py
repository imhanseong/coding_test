import sys								
input = sys.stdin.readline				

for _ in range(3):						
    n = int(input())					
    sum = 0								
    for i in range(n):					
        n_input = int(input())			
        sum += n_input					
    if sum == 0:						
        print("0")
    elif sum > 0:
        print("+")
    elif sum < 0:
        print("-")