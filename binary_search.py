
def binary_search(li, elem):
	l=0
	r=len(li)-1
	while True:
		n=(l+r)/2
		if li[n]<elem:
			l=n+1
		else:
			r=n-1
		if li[n] is elem:
			flag=True
			break
		elif n is l or n is r:
			flag=False
			break
	if flag:
		print elem, "Found at:", n
	else:
		print "Nt prsent"

def main():
	li=[1,2,3,4,5,7,8,9]
	elem=1
	binary_search(li, elem)
	

if __name__ == "__main__":
	main()
