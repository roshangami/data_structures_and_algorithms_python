
class Node():
	def __init__(self, nodeval, nextnode=None):
		self.nodeval=nodeval
		self.nextnode=nextnode

class LinkedList():
	def __init__(self):
		self.last=None
		self.size=0

	def add_node(self, node):
		if self.last is None:
			self.last=node
		else:
			node.nextnode=self.last
			self.last=node
		self.size=self.size+1

	def print_list(self):
		start = self.last
		while True:
			print start.nodeval,
			if start.nextnode is None:
				break
			print "->",
			start=start.nextnode
		print ''
	def delete_node(self, nodeval):
		start=self.last
		if start.nodeval is nodeval:
			self.last=start.nextnode
		while True:
			if start.nextnode is None:
				print "Error: Element not found"
				break
			elif start.nextnode.nodeval is nodeval:
				start.nextnode=start.nextnode.nextnode
				break
			start=start.nextnode

	def print_reverse(self, start=None):
		if start is None: start=self.last
		if start.nextnode != None:
			self.print_reverse(start.nextnode)
		print start.nodeval,

	def reverse_recursion(self, start=None):
		if start is None:
			start=self.last
		if start.nextnode != None:
			self.reverse_recursion(start.nextnode)
			start.nextnode.nextnode=start
			start.nextnode=None
		else:
			self.last=start
			return

	def reverse_iterative(self):
		start=self.last
		for val in range(self.size)[::-1]:
			num=val
#			print "val",val
			while num:
#				print "num",num
				if start.nextnode is not None:
#					print "start.nodeval", start.nodeval
					start.nodeval,start.nextnode.nodeval = start.nextnode.nodeval,start.nodeval
					start=start.nextnode
				num=num-1
			start=self.last
def main():
	n1=Node("Mon")
	n2=Node("Tue")
	n3=Node("Wed")
	n4=Node("Thus")
	n5=Node("Fri")
	ll=LinkedList()
	ll.add_node(n1)
	ll.add_node(n2)
	ll.add_node(n3)
	ll.add_node(n4)
	ll.add_node(n5)
	ll.print_list()
#	ll.delete_node("Wedsd")
#	ll.print_list()
#	ll.reverse_iterative()
#	ll.print_list()
	ll.reverse_recursion()
	ll.print_list()

if __name__ == "__main__":
	main()
