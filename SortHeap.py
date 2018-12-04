
class Heap():
	def __init__(self, li):
		self.li=li

	def heap_sort(self):
		n=len(self.li)
		for i in range(n-1, -1, -1):
			self.heapify(i)
		for i in range(n-1, -1, -1):
			self.li[0], self.li[i] = self.li[i], self.li[0]
			print self.li.pop(),
			self.heapify(0)

	def heapify(self, i):
		n=len(self.li)
		l=2*i+1
		r=2*i+2
		largest=i
		if l<n and self.li[l]>self.li[i]:
			largest=l
		if r<n and self.li[largest]<self.li[r]:
			largest=r
		if largest is not i:
			self.li[largest], self.li[i] = self.li[i], self.li[largest]
			self.heapify(largest)


def main():
	li=[4,3,1,5,9,7,8,2,6]
	print li
	h=Heap(li)
	h.heap_sort()
	
if __name__ == "__main__":
	main()
