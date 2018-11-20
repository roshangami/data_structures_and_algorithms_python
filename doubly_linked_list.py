
class Node():
	def __init__(self, nodeval, prevnode=None, nextnode=None):
		self.nodeval=nodeval
		self.prevnode=prevnode
		self.nextnode=nextnode

class DoublyLinkedList():
	def __init__(self):
		self.last=None
		self.first=None
		self.size=0

	def add_front(self, node):
		start=self.last
		if start is None:
			self.last=node
			self.first=node
		else:
			node.nextnode=start
			start.prevnode=node
			self.last=node

	def add_rear(self, node):
		start=self.first
		if start is  None:
			self.last=node
			self.first=node
		else:
			node.prevnode=start
			start.nextnode=node
			self.first=node

	def print_list(self):
		start=self.last
		while start is not None:
			print start.nodeval,
			if start.nextnode is not None:
				print "->",
			start=start.nextnode

	def print_reverse_list(self):
		start=self.first
		while start is not None:
			print start.nodeval,
			if start.prevnode is not None:
				print "->",
			start=start.prevnode

	def search_node(self, nodeval):
		start=self.last
		while True:
			if start is None:
				print nodeval, 'Not present'
				break
			if start.nodeval is nodeval:
				print start.nodeval, 'Present'
				return start
			start=start.nextnode

	def insert_node(self, node, af_node):
		insert_af=self.search_node(af_node)
		if type(insert_af) is 'str':
			print insert_af
		insert_af.nextnode.prevnode=node
		node.nextnode=insert_af.nextnode
		node.prevnode=insert_af
		insert_af.nextnode=node

def main():
	n1=Node("Mon")
	n2=Node("Tue")
	n3=Node("Wed")
	dll=DoublyLinkedList()
	dll.add_front(n2)
	dll.add_rear(n1)
	dll.add_front(n3)
	dll.print_list()
	print ''
	dll.print_reverse_list()
	dll.search_node("Mon")
	dll.insert_node(Node("0"), "Tue")
	dll.print_list()

if __name__ == "__main__":
	main()
