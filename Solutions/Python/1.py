
def sumExists(l , k):
	hashmap = {}
	for i in range(len(l)):
		if (hashmap.get(k - l[i]) != None):
			return True
		hashmap[l[i]] = 1
	return False



if __name__ == "__main__":
	l = [int(x) for x in input().split()]
	k = int(input())
	print(sumExists(l,k))