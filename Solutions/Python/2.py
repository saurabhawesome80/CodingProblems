l = [int(x) for x in input().split()]
rl =[1]
prod = 1
for i in range(len(l)-1):
	rl.append(prod*l[i])
	prod *=l[i]

prod = l[len(l)-1]
for j in range(len(l)-1,0,-1):
	rl[j-1] =  rl[j-1]*prod
	prod *= l[j-1]

print(rl)