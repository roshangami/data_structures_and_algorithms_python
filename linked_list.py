
class Node():
	def __init__(self, nodeval, nextnode=None):
		self.nodeval=nodeval
		self.nextnode=nextnode

class LinkedList():
	def __init__(self):
		self.last=None

	def add_node(self, node):
		if self.last is None:
			self.last=node
		else:
			node.nextnode=self.last
			self.last=node
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
			start=start.nextnode
			self.print_reverse(start)
			print start.nodeval,
		if start.nodeval is self.last.nodeval:
			print self.last.nodeval,
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
	ll.print_reverse()

if __name__ == "__main__":
	main()
