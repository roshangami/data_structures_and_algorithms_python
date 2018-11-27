

def merge(l,m,r):
	L=li[l:m+1]
	R=li[m+1:r+1]
	print "left", L
	print "right", R
	i=j=k=0
	while i<len(L) and j < len(R):
		if L[i]<R[j]:
			li[k]=L[i]
			i=i+1
		else:
			li[k]=R[j]
			j=j+1
		k=k+1
	while i < len(L):
		li[k]=L[i]
		i=i+1
		k=k+1
	while j < len(R):
		li[k]=R[j]
		j=j+1
		k=k+1
	print li
def main(li):
	print "before sorting:",li
	merge_sort(0,len(li)-1)
	print "after sorting:",li

def merge_sort(l,r):
	if l < r:
		m=(l+r)/2
		merge_sort(l,m)
		merge_sort(m+1,r)
		merge(l,m,r)

if __name__ == "__main__":
	li=[5,4,3,1,2]
	main(li)
