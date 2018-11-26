
def quick(s, e):
	pointer=s
	for val in li[s:e]:
		if li[e] > val:
			ind=li.index(val)
			print li[pointer], li[ind]
			li[pointer],li[ind]=li[ind],li[pointer]
			pointer=pointer+1
	li[pointer], li[e]=li[e], li[pointer]
	print li
	if s<pointer:
		quick(s, pointer-1)
	if pointer<e:
		quick(pointer+1, e)

def main():
	print li
#	val=li[6]
#	pointer=0
#	li[pointer], li[li.index(val)]=li[li.index(val)],li[pointer]
	quick(0, len(li)-1)
	print li

if __name__ == "__main__":
	li=[5,2,6,9,3,8,1,4,7]
	main()
