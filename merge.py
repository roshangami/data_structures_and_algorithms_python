

def merge(li,l,m,r):
	i=j=k=0
 
def main(li):
	print "before sorting:",li
	merge_sort(li,0,len(li)-1)
	print "after sorting:",li

def merge_sort(li,l,r):
	if l < r:
		m=(l+(r-1))/2
		merge_sort(li,l,m)
		merge_sort(li,m+1,r)
		print "true",li[l:r+1]
	else:
		print li[l],li[r]
if __name__ == "__main__":
	li=[5,4,3,1,2]
	main(li)
