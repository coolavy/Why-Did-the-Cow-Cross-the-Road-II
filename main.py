import sys

sys.stdin = open('circlecross.in', 'r')
sys.stdout = open('circlecross.out', 'w')

road = input()

ans = 0

for x in range(len(road)):
	for y in range(x + 1, len(road)):
		for z in range(y + 1, len(road)):
			for a in range(z + 1, len(road)):
			    if (road[x] == road[z]) and  (road[y] == road[a]):
				    ans += 1
				    
print(ans)