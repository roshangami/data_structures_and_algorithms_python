
def printHeap():
	global li
	for i in range(len(li)-1, -1, -1):
		try:
			l=li[2*i+1]
		except Exception as e:
			l='None'
		try:
			r=li[2*i+2]
		except Exception as e:
			r='None'
		print li[i], "left->", l, "right->", r

def heapify(n, i):
	global li
	largest=i
	l=2*i+1
	r=2*i+2
	
	if l<n and li[l]>li[i]:
		largest=i
	if r<n and li[largest]<li[r]:
		largest=r
	if largest is not i:
		li[largest], li[i] = li[i], li[largest]
		heapify(n, largest)
	

def heapSort():
	global li
	n=len(li)
	for i in range(n-1, -1, -1):
		heapify(n, i)
	printHeap()


def main():
	global li
	print li
	heapSort()
	printHeap()

if __name__ == "__main__":
	li=[7,9,5,8,4,3,1,2,5,6]
	main()
